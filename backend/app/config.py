"""
━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Application Configuration with Pydantic Settings

This module centralizes ALL configuration for the backend. Settings are
loaded from environment variables (the .env file), with sensible defaults
for local development.

Compare with ASP.NET:
- This replaces IConfiguration + appsettings.json
- In .NET: services.Configure<AppSettings>(configuration);
- In FastAPI: settings = Settings() — that's it!

Pydantic Settings features:
- Type validation (env var "true" → Python bool True)
- Default values for development
- Automatic .env file loading
- Nested settings with prefixes

Key insight: In Python, we don't use dependency injection for configuration.
We create a single `settings` instance at module level and import it directly.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    All values can be overridden via .env file or environment variables.
    Environment variables take precedence over .env file values.
    """

    # ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # model_config tells Pydantic Settings HOW to load the configuration.
    # - env_file: Load from .env file in the project root
    # - env_file_encoding: File encoding (UTF-8 is standard)
    # - case_sensitive: Whether env var names are case-sensitive
    # - extra: What to do with unknown env vars ("ignore" = skip them)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Application ────────────────────────────────────────────────────
    APP_NAME: str = "DevBrain"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # ── Backend Server ─────────────────────────────────────────────────
    BACKEND_PORT: int = 8000
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_CORS_ORIGINS: str = "http://localhost:3000"

    # ── Database ───────────────────────────────────────────────────────
    POSTGRES_USER: str = "devbrain"
    POSTGRES_PASSWORD: str = "devbrain_secret"
    POSTGRES_DB: str = "devbrain"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str = (
        "postgresql+asyncpg://devbrain:devbrain_secret@localhost:5432/devbrain"
    )
    TEST_DATABASE_URL: str = (
        "postgresql+asyncpg://devbrain:devbrain_secret@localhost:5432/devbrain_test"
    )

    # ── Redis ──────────────────────────────────────────────────────────
    REDIS_URL: str = "redis://localhost:6379/0"

    # ── AI Providers ───────────────────────────────────────────────────
    GOOGLE_API_KEY: str = ""
    GROQ_API_KEY: str = ""
    HUGGINGFACE_API_KEY: str = ""

    # ── Authentication ─────────────────────────────────────────────────
    AUTH_SECRET: str = ""

    @property
    def cors_origins(self) -> list[str]:
        """Parse CORS origins from comma-separated string to list."""
        return [
            origin.strip()
            for origin in self.BACKEND_CORS_ORIGINS.split(",")
            if origin.strip()
        ]

    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.APP_ENV == "development"


# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Create a single settings instance. This is imported throughout the app:
#   from app.config import settings
#
# Compare with ASP.NET:
#   In .NET, you'd inject IConfiguration or IOptions<T> via constructor DI.
#   In Python/FastAPI, we just import this module-level instance.
#   Both approaches work — Python's is simpler, .NET's is more testable.
#
# For testing, you can override settings by setting env vars before import,
# or by using FastAPI's dependency override system.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
settings = Settings()
