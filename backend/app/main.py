"""
━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DevBrain Backend — FastAPI Application Entry Point

This is the main entry point for the backend application. In ASP.NET terms,
this is your Program.cs + Startup.cs combined.

FastAPI key concepts:
- `app = FastAPI()` creates the application (like `builder.Build()` in .NET)
- Routers are registered with `app.include_router()` (like `MapControllers()`)
- Middleware is added with `app.add_middleware()` (like `app.UseXxx()`)
- Lifespan events handle startup/shutdown (like `IHostedService`)

Current state: Phase 0 — Minimal health check endpoint.
More features will be added as you progress through the phases.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import collections, documents
from app.config import settings
from app.core.database import engine


# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Lifespan: Manages startup and shutdown events for the application.
#
# In ASP.NET, you might use IHostedService or configure services in
# ConfigureServices(). Here, the `lifespan` context manager handles:
# - Startup: Database connections, cache warming, etc.
# - Shutdown: Graceful cleanup of connections and resources
#
# The `yield` statement separates startup (before) from shutdown (after).
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan: startup and shutdown events."""
    # ── Startup ─────────────────────────────────────────────
    # TODO(PHASE-4): Initialize LiteLLM configuration
    # TODO(PHASE-6): Initialize Celery worker
    print("🧠 DevBrain backend starting up...")

    yield  # Application is running

    # ── Shutdown ────────────────────────────────────────────
    # TODO(PHASE-4): Cleanup AI resources
    await engine.dispose()
    print("🧠 DevBrain backend shutting down...")


# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Create the FastAPI application instance.
#
# Compare with ASP.NET Program.cs:
#   var builder = WebApplication.CreateBuilder(args);
#   var app = builder.Build();
#
# The parameters here are equivalent to:
# - title → used in Swagger/OpenAPI docs
# - description → shown in API documentation
# - version → API version
# - lifespan → startup/shutdown hooks
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
app = FastAPI(
    title=settings.APP_NAME,
    description="AI-Powered Document Intelligence Platform",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",  # Swagger UI (like Swagger in ASP.NET)
    redoc_url="/redoc",  # Alternative docs UI
)


# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CORS Middleware: Controls which origins can access your API.
#
# In ASP.NET: app.UseCors(policy => policy.WithOrigins(...))
# In FastAPI: CORSMiddleware with allow_origins
#
# During development, we allow the Next.js dev server (localhost:3000)
# to call our API (localhost:8000). Without this, browsers block
# cross-origin requests for security.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ──────────────────────────────────────────────────────────────────────────────
# Health Check Endpoint
#
# LEARN: A health check is a simple endpoint that confirms the service is
# running. It's used by:
# - Docker healthcheck (in docker-compose.yml)
# - Load balancers (to route traffic away from unhealthy instances)
# - Monitoring systems (to alert when the service is down)
# - Your own verification tests (Phase 0 check!)
#
# Compare with ASP.NET: app.MapHealthChecks("/health")
# ──────────────────────────────────────────────────────────────────────────────
@app.get("/health", tags=["system"])
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns the application status. Used by Docker healthcheck,
    load balancers, and monitoring systems.
    """
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": "0.1.0",
    }


# ── API Routers (Phase 1) ────────────────────────────────────────────────────
app.include_router(documents.router, prefix="/api/v1")
app.include_router(collections.router, prefix="/api/v1")

# CHECK(PHASE-1): Start with `make dev-backend`
# ✅ http://localhost:8000/docs should show document and collection endpoints
# ✅ make verify-phase1 should pass all tests
