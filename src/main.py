"""
Research Papers API — academic paper access with pay-per-read via Mainlayer.

Free endpoints:
  GET /papers                 — list all papers (metadata + abstract)
  GET /papers/search?q=       — search papers
  GET /papers/{id}            — paper detail (abstract)
  GET /categories             — list categories

Paid endpoint ($0.05 per paper):
  GET /papers/{id}/full       — full paper text
    Requires: X-Payer-Wallet header
    Returns:  402 Payment Required if no entitlement found
"""

import logging
import os
from typing import List, Optional

from fastapi import Depends, FastAPI, Header, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.mainlayer import MainlayerClient, get_mainlayer_client
from src.models import (
    Category,
    HealthCheck,
    PaperDetail,
    PaperFullText,
    PaperSummary,
    PaymentRequired,
    SearchResult,
)
from src.papers_db import (
    Author,
    CATEGORY_BY_ID,
    get_all_papers,
    get_category_paper_counts,
    get_paper_detail,
    get_paper_full_text,
    search_papers,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(
    title="Research Papers API",
    description=(
        "Academic paper database for AI agents. "
        "Browse and search papers for free; pay $0.05 to access full text. "
        "Powered by Mainlayer — payment infrastructure for AI agents."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

PAPER_PRICE_USD = 0.05


# ---------------------------------------------------------------------------
# Routes — health
# ---------------------------------------------------------------------------


@app.get("/health", response_model=HealthCheck, tags=["system"])
async def health() -> HealthCheck:
    """Service health check."""
    return HealthCheck()


# ---------------------------------------------------------------------------
# Routes — papers (free)
# ---------------------------------------------------------------------------


@app.get("/papers", response_model=List[PaperSummary], tags=["papers"])
async def list_papers() -> List[PaperSummary]:
    """
    List all available papers.

    Returns id, title, authors, abstract, price, and category for every
    paper in the database. Full text requires a separate paid request.
    """
    return get_all_papers()


@app.get("/papers/search", response_model=SearchResult, tags=["papers"])
async def search(q: str = Query(..., min_length=1, description="Search query")) -> SearchResult:
    """
    Full-text search across title, abstract, keywords, authors, and category.

    Free endpoint — returns paper summaries without full text.
    """
    results = search_papers(q)
    return SearchResult(query=q, total=len(results), papers=results)


@app.get("/papers/{paper_id}", response_model=PaperDetail, tags=["papers"])
async def get_paper(paper_id: str) -> PaperDetail:
    """
    Get detailed metadata for a single paper including abstract.

    Free endpoint — does not include full text.
    """
    paper = get_paper_detail(paper_id)
    if paper is None:
        raise HTTPException(status_code=404, detail=f"Paper '{paper_id}' not found.")
    return paper


# ---------------------------------------------------------------------------
# Routes — full text (paid)
# ---------------------------------------------------------------------------


@app.get(
    "/papers/{paper_id}/full",
    response_model=PaperFullText,
    responses={
        402: {
            "model": PaymentRequired,
            "description": "Payment required to access full paper text.",
        },
        404: {"description": "Paper not found."},
    },
    tags=["papers"],
)
async def get_paper_full(
    paper_id: str,
    x_payer_wallet: Optional[str] = Header(
        default=None,
        description=(
            "Your Mainlayer wallet identifier. Required to pay $0.05 for full paper access."
        ),
    ),
    mainlayer: MainlayerClient = Depends(get_mainlayer_client),
) -> PaperFullText:
    """
    Get the full text of an academic paper.

    **Costs $0.05 per access via Mainlayer.**

    Include your `X-Payer-Wallet` header with your Mainlayer wallet ID.
    If you don't have a wallet yet, the 402 response will include a
    `payment_url` where you can set one up.

    AI agents should:
    1. Make this request (will receive 402 if not yet paid)
    2. Navigate to the `payment_url` in the 402 response
    3. Complete payment via Mainlayer
    4. Re-issue this request — access will be granted automatically
    """
    raw = get_paper_full_text(paper_id)
    if raw is None:
        raise HTTPException(status_code=404, detail=f"Paper '{paper_id}' not found.")

    # Require wallet header
    if not x_payer_wallet:
        payment_url = mainlayer.payment_url(resource_id=paper_id, price_usd=PAPER_PRICE_USD)
        return JSONResponse(
            status_code=402,
            content=PaymentRequired(
                message=(
                    f"Full text access costs ${PAPER_PRICE_USD:.2f}. "
                    "Provide your X-Payer-Wallet header and complete payment at the payment_url."
                ),
                price_usd=PAPER_PRICE_USD,
                paper_id=paper_id,
                payment_url=payment_url,
            ).model_dump(),
        )

    # Verify entitlement with Mainlayer
    entitled = await mainlayer.check_entitlement(
        payer_wallet=x_payer_wallet,
        resource_id=paper_id,
        price_usd=PAPER_PRICE_USD,
    )

    if not entitled:
        payment_url = mainlayer.payment_url(resource_id=paper_id, price_usd=PAPER_PRICE_USD)
        logger.info(
            "Payment required for paper=%s wallet=%s", paper_id, x_payer_wallet
        )
        return JSONResponse(
            status_code=402,
            content=PaymentRequired(
                message=(
                    f"Payment of ${PAPER_PRICE_USD:.2f} required to access '{raw['title']}'. "
                    "Visit the payment_url to complete your purchase."
                ),
                price_usd=PAPER_PRICE_USD,
                paper_id=paper_id,
                payment_url=payment_url,
            ).model_dump(),
        )

    logger.info("Serving full text for paper=%s wallet=%s", paper_id, x_payer_wallet)
    return PaperFullText(
        id=raw["id"],
        title=raw["title"],
        authors=[Author(**a) for a in raw["authors"]],
        abstract=raw["abstract"],
        year=raw["year"],
        category=raw["category"],
        price_usd=PAPER_PRICE_USD,
        doi=raw.get("doi"),
        keywords=raw.get("keywords", []),
        citations=raw.get("citations", 0),
        journal=raw.get("journal"),
        full_text=raw["full_text"],
    )


# ---------------------------------------------------------------------------
# Routes — categories (free)
# ---------------------------------------------------------------------------


@app.get("/categories", response_model=List[Category], tags=["categories"])
async def list_categories() -> List[Category]:
    """
    List all paper categories with paper counts.

    Free endpoint.
    """
    counts = get_category_paper_counts()
    return [
        Category(
            id=cat["id"],
            name=cat["name"],
            description=cat["description"],
            paper_count=counts.get(cat["id"], 0),
        )
        for cat in CATEGORY_BY_ID.values()
    ]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        reload=os.getenv("ENV", "production") == "development",
    )
