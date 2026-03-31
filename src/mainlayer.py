"""
Mainlayer payment client.

Verifies payment entitlements via the Mainlayer API before serving
gated content. Mainlayer is payment infrastructure for AI agents —
think of it as Stripe for AI agents.
"""

import os
import logging
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

MAINLAYER_BASE_URL = os.getenv("MAINLAYER_BASE_URL", "https://api.mainlayer.fr")
MAINLAYER_API_KEY = os.getenv("MAINLAYER_API_KEY", "")

# Price per full paper access in USD
PAPER_PRICE_USD = 0.05


class MainlayerError(Exception):
    """Raised when the Mainlayer API returns an unexpected error."""


class MainlayerClient:
    """Thin async client for the Mainlayer payment API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 10.0,
    ) -> None:
        self.api_key = api_key or MAINLAYER_API_KEY
        self.base_url = (base_url or MAINLAYER_BASE_URL).rstrip("/")
        self.timeout = timeout

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    async def check_entitlement(
        self,
        payer_wallet: str,
        resource_id: str,
        price_usd: float = PAPER_PRICE_USD,
    ) -> bool:
        """
        Return True if the given payer wallet has an entitlement for
        resource_id at the requested price.

        Entitlement is confirmed when Mainlayer returns:
          { "entitled": true, ... }
        """
        try:
            async with self._client() as client:
                response = await client.post(
                    f"{self.base_url}/v1/entitlements/check",
                    json={
                        "payer_wallet": payer_wallet,
                        "resource_id": resource_id,
                        "price_usd": price_usd,
                    },
                )

                if response.status_code == 200:
                    data = response.json()
                    return bool(data.get("entitled", False))

                if response.status_code == 402:
                    # Not entitled — caller should return 402 to the agent
                    return False

                # Unexpected status — log and deny access conservatively
                logger.error(
                    "Mainlayer entitlement check returned unexpected status %s: %s",
                    response.status_code,
                    response.text,
                )
                return False

        except httpx.TimeoutException:
            logger.error("Mainlayer entitlement check timed out for wallet=%s", payer_wallet)
            return False
        except httpx.RequestError as exc:
            logger.error("Mainlayer request error: %s", exc)
            return False

    def payment_url(self, resource_id: str, price_usd: float = PAPER_PRICE_USD) -> str:
        """
        Return the Mainlayer payment URL that an AI agent should visit
        to purchase access to a resource.
        """
        return (
            f"{self.base_url}/pay"
            f"?resource_id={resource_id}"
            f"&price_usd={price_usd:.2f}"
            f"&api_key={self.api_key}"
        )

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _client(self) -> httpx.AsyncClient:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return httpx.AsyncClient(headers=headers, timeout=self.timeout)


# ---------------------------------------------------------------------------
# Module-level singleton (used by FastAPI dependency injection)
# ---------------------------------------------------------------------------

_default_client: Optional[MainlayerClient] = None


def get_mainlayer_client() -> MainlayerClient:
    """FastAPI dependency that returns a shared MainlayerClient instance."""
    global _default_client
    if _default_client is None:
        _default_client = MainlayerClient()
    return _default_client
