"""
Tests for the Research Papers API.

Covers:
  - Free endpoints (papers list, detail, search, categories, health)
  - Paid endpoint (full text) — 402 when no wallet, 402 when not entitled,
    200 when entitled
  - Edge cases (unknown IDs, empty search, missing query param)
"""

import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient

from src.main import app, PAPER_PRICE_USD
from src.mainlayer import MainlayerClient


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def client():
    """Return a synchronous TestClient for the FastAPI app."""
    with TestClient(app) as c:
        yield c


def _entitled_mainlayer() -> MainlayerClient:
    """Return a mock MainlayerClient that always grants entitlement."""
    ml = MainlayerClient.__new__(MainlayerClient)
    ml.check_entitlement = AsyncMock(return_value=True)
    ml.payment_url = lambda resource_id, price_usd=PAPER_PRICE_USD: (
        f"https://api.mainlayer.fr/pay?resource_id={resource_id}&price_usd={price_usd:.2f}"
    )
    return ml


def _denied_mainlayer() -> MainlayerClient:
    """Return a mock MainlayerClient that always denies entitlement."""
    ml = MainlayerClient.__new__(MainlayerClient)
    ml.check_entitlement = AsyncMock(return_value=False)
    ml.payment_url = lambda resource_id, price_usd=PAPER_PRICE_USD: (
        f"https://api.mainlayer.fr/pay?resource_id={resource_id}&price_usd={price_usd:.2f}"
    )
    return ml


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------


def test_health_returns_ok(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert body["service"] == "research-papers-api"
    assert "version" in body


# ---------------------------------------------------------------------------
# GET /papers
# ---------------------------------------------------------------------------


def test_list_papers_returns_200(client):
    resp = client.get("/papers")
    assert resp.status_code == 200


def test_list_papers_returns_list(client):
    resp = client.get("/papers")
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == 20


def test_list_papers_have_required_fields(client):
    resp = client.get("/papers")
    paper = resp.json()[0]
    for field in ("id", "title", "authors", "abstract", "year", "category", "price_usd"):
        assert field in paper, f"Missing field: {field}"


def test_list_papers_price_is_five_cents(client):
    resp = client.get("/papers")
    for paper in resp.json():
        assert paper["price_usd"] == pytest.approx(0.05)


def test_list_papers_no_full_text_field(client):
    resp = client.get("/papers")
    for paper in resp.json():
        assert "full_text" not in paper


def test_list_papers_authors_are_objects(client):
    resp = client.get("/papers")
    for paper in resp.json():
        for author in paper["authors"]:
            assert "name" in author


# ---------------------------------------------------------------------------
# GET /papers/{id}
# ---------------------------------------------------------------------------


def test_paper_detail_known_id(client):
    resp = client.get("/papers/paper-001")
    assert resp.status_code == 200


def test_paper_detail_has_keywords(client):
    resp = client.get("/papers/paper-001")
    data = resp.json()
    assert "keywords" in data
    assert isinstance(data["keywords"], list)


def test_paper_detail_has_citations(client):
    resp = client.get("/papers/paper-001")
    data = resp.json()
    assert "citations" in data
    assert data["citations"] > 0


def test_paper_detail_no_full_text(client):
    resp = client.get("/papers/paper-001")
    assert "full_text" not in resp.json()


def test_paper_detail_unknown_id_returns_404(client):
    resp = client.get("/papers/does-not-exist")
    assert resp.status_code == 404


def test_paper_detail_last_paper(client):
    resp = client.get("/papers/paper-020")
    assert resp.status_code == 200
    assert "Toolformer" in resp.json()["title"]


# ---------------------------------------------------------------------------
# GET /papers/search
# ---------------------------------------------------------------------------


def test_search_returns_results(client):
    resp = client.get("/papers/search?q=transformer")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] > 0
    assert len(data["papers"]) == data["total"]


def test_search_result_has_query_field(client):
    resp = client.get("/papers/search?q=attention")
    data = resp.json()
    assert data["query"] == "attention"


def test_search_no_results_for_gibberish(client):
    resp = client.get("/papers/search?q=zzzzxxxxxnotexist")
    assert resp.status_code == 200
    assert resp.json()["total"] == 0


def test_search_missing_q_param_returns_422(client):
    resp = client.get("/papers/search")
    assert resp.status_code == 422


def test_search_case_insensitive(client):
    resp_lower = client.get("/papers/search?q=bert")
    resp_upper = client.get("/papers/search?q=BERT")
    assert resp_lower.json()["total"] == resp_upper.json()["total"]


def test_search_by_author(client):
    resp = client.get("/papers/search?q=Vaswani")
    data = resp.json()
    assert data["total"] >= 1


# ---------------------------------------------------------------------------
# GET /categories
# ---------------------------------------------------------------------------


def test_categories_returns_200(client):
    resp = client.get("/categories")
    assert resp.status_code == 200


def test_categories_returns_list(client):
    categories = client.get("/categories").json()
    assert isinstance(categories, list)
    assert len(categories) > 0


def test_categories_have_required_fields(client):
    for cat in client.get("/categories").json():
        for field in ("id", "name", "description", "paper_count"):
            assert field in cat


def test_categories_paper_counts_sum_to_total(client):
    total_papers = len(client.get("/papers").json())
    total_from_categories = sum(c["paper_count"] for c in client.get("/categories").json())
    assert total_from_categories == total_papers


# ---------------------------------------------------------------------------
# GET /papers/{id}/full — 402 cases
# ---------------------------------------------------------------------------


def test_full_text_no_wallet_returns_402(client):
    resp = client.get("/papers/paper-001/full")
    assert resp.status_code == 402


def test_full_text_no_wallet_returns_payment_required_body(client):
    resp = client.get("/papers/paper-001/full")
    body = resp.json()
    assert body["error"] == "payment_required"
    assert "payment_url" in body
    assert body["price_usd"] == pytest.approx(0.05)


def test_full_text_with_wallet_not_entitled_returns_402(client):
    from src.main import get_mainlayer_client

    app.dependency_overrides[get_mainlayer_client] = lambda: _denied_mainlayer()
    try:
        resp = client.get(
            "/papers/paper-001/full",
            headers={"X-Payer-Wallet": "wallet-abc-123"},
        )
        assert resp.status_code == 402
    finally:
        app.dependency_overrides.clear()


def test_full_text_not_entitled_body_has_payment_url(client):
    from src.main import get_mainlayer_client

    app.dependency_overrides[get_mainlayer_client] = lambda: _denied_mainlayer()
    try:
        resp = client.get(
            "/papers/paper-001/full",
            headers={"X-Payer-Wallet": "wallet-abc-123"},
        )
        body = resp.json()
        assert "payment_url" in body
        assert "paper_id" in body
    finally:
        app.dependency_overrides.clear()


def test_full_text_unknown_paper_returns_404(client):
    from src.main import get_mainlayer_client

    app.dependency_overrides[get_mainlayer_client] = lambda: _entitled_mainlayer()
    try:
        resp = client.get(
            "/papers/no-such-paper/full",
            headers={"X-Payer-Wallet": "wallet-abc-123"},
        )
        assert resp.status_code == 404
    finally:
        app.dependency_overrides.clear()


# ---------------------------------------------------------------------------
# GET /papers/{id}/full — 200 (entitled) cases
# ---------------------------------------------------------------------------


def test_full_text_entitled_returns_200(client):
    from src.main import get_mainlayer_client

    app.dependency_overrides[get_mainlayer_client] = lambda: _entitled_mainlayer()
    try:
        resp = client.get(
            "/papers/paper-001/full",
            headers={"X-Payer-Wallet": "wallet-entitled-456"},
        )
        assert resp.status_code == 200
    finally:
        app.dependency_overrides.clear()


def test_full_text_entitled_response_has_full_text(client):
    from src.main import get_mainlayer_client

    app.dependency_overrides[get_mainlayer_client] = lambda: _entitled_mainlayer()
    try:
        resp = client.get(
            "/papers/paper-001/full",
            headers={"X-Payer-Wallet": "wallet-entitled-456"},
        )
        body = resp.json()
        assert "full_text" in body
        assert len(body["full_text"]) > 100
    finally:
        app.dependency_overrides.clear()


def test_full_text_entitled_has_all_metadata(client):
    from src.main import get_mainlayer_client

    app.dependency_overrides[get_mainlayer_client] = lambda: _entitled_mainlayer()
    try:
        resp = client.get(
            "/papers/paper-001/full",
            headers={"X-Payer-Wallet": "wallet-entitled-456"},
        )
        body = resp.json()
        for field in ("id", "title", "authors", "abstract", "year", "category",
                      "keywords", "citations", "full_text"):
            assert field in body, f"Missing field: {field}"
    finally:
        app.dependency_overrides.clear()


def test_full_text_correct_paper_returned(client):
    from src.main import get_mainlayer_client

    app.dependency_overrides[get_mainlayer_client] = lambda: _entitled_mainlayer()
    try:
        resp = client.get(
            "/papers/paper-009/full",
            headers={"X-Payer-Wallet": "wallet-entitled-456"},
        )
        body = resp.json()
        assert body["id"] == "paper-009"
        assert "GPT-3" in body["title"] or "Few-Shot" in body["title"]
    finally:
        app.dependency_overrides.clear()
