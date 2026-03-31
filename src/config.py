import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mainlayer_api_key: str = ""
    mainlayer_base_url: str = "https://api.mainlayer.fr"
    resource_id_abstract: str = "research-paper-abstract-v1"
    resource_id_full_text: str = "research-paper-full-text-v1"
    price_abstract_usdc: float = 0.001
    price_full_text_usdc: float = 0.01
    entitlement_cache_ttl_seconds: int = 300
    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
