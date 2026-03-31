"""Pydantic models for the Research Papers API."""

from typing import List, Optional
from pydantic import BaseModel, Field


class Author(BaseModel):
    name: str
    affiliation: Optional[str] = None


class PaperSummary(BaseModel):
    """Lightweight paper representation returned in list/search endpoints."""

    id: str
    title: str
    authors: List[Author]
    abstract: str
    year: int
    category: str
    price_usd: float = Field(default=0.05, description="Cost in USD to access full text")
    doi: Optional[str] = None


class PaperDetail(PaperSummary):
    """Full paper metadata (no full text — still requires payment)."""

    keywords: List[str] = []
    citations: int = 0
    journal: Optional[str] = None


class PaperFullText(PaperDetail):
    """Complete paper including full text — returned only after payment."""

    full_text: str


class Category(BaseModel):
    id: str
    name: str
    description: str
    paper_count: int


class SearchResult(BaseModel):
    query: str
    total: int
    papers: List[PaperSummary]


class PaymentRequired(BaseModel):
    error: str = "payment_required"
    message: str
    price_usd: float
    paper_id: str
    payment_url: str


class HealthCheck(BaseModel):
    status: str = "ok"
    service: str = "research-papers-api"
    version: str = "1.0.0"
