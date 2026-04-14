# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Dockerfile: Backend Container Definition
#
# A Dockerfile is a recipe for building a container image. Each instruction
# creates a "layer" — Docker caches these layers, so unchanged steps
# don't need to rebuild. Order matters for cache efficiency!
#
# Compare with ASP.NET:
# - In .NET, you'd use `mcr.microsoft.com/dotnet/aspnet` as base image
# - Here, we use a slim Python image (much smaller)
# - The multi-stage pattern is the same: build → production
#
# Best practices applied here:
# 1. Use slim base image (smaller attack surface, faster pulls)
# 2. Install deps BEFORE copying code (better cache utilization)
# 3. Run as non-root user (security)
# 4. Use .dockerignore to exclude unnecessary files
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── Stage 1: Build ─────────────────────────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app

# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Install uv globally. We use pipx-style install to get the latest version.
# uv is dramatically faster than pip for installing packages.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Copy ONLY dependency files first. Docker caches this layer, so if your
# dependencies haven't changed, it won't reinstall them — even if your
# code changed. This saves minutes on rebuilds.
#
# This is like .NET's two-step restore:
#   COPY *.csproj ./        ← copy project files
#   RUN dotnet restore      ← restore NuGet packages (cached)
#   COPY . .                ← then copy source code
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev --no-install-project

# Copy the rest of the application code
COPY . .

# ── Stage 2: Production ───────────────────────────────────────────────
FROM python:3.12-slim AS production

WORKDIR /app

# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Security: Create a non-root user. Running containers as root is a
# security risk — if an attacker exploits your app, they'd have
# root access to the container.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup --create-home appuser

# Copy uv from builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy the virtual environment from builder (with all deps installed)
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app

# Set the virtual environment path
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Switch to non-root user
USER appuser

EXPOSE 8000

# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Start the FastAPI app with uvicorn.
# --host 0.0.0.0 : Listen on all interfaces (required in Docker)
# --port 8000    : The port we expose
# --workers 4    : Number of worker processes (for production)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

