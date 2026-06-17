from functools import lru_cache
from typing import Literal

from pydantic import AnyHttpUrl, Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    PROJECT_NAME: str = "FoodAI"
    VERSION: str = "0.1.0"
    ENVIRONMENT: Literal["local", "test", "staging", "production"] = "local"
    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: PostgresDsn | str = (
        "postgresql+asyncpg://foodai:foodai@localhost:5432/foodai"
    )

    SECRET_KEY: str = Field(default="change-me-in-production", min_length=16)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"

    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl | str] = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
