# Phase 0: Foundations & Environment 🔧

> **Mode**: 🟢 Guided  
> **Duration**: 2-3 days  
> **Prerequisites**: A computer with macOS, admin access, and internet

## Learning Objectives

By the end of this phase, you will:
1. Understand the monorepo structure and why each file exists
2. Run PostgreSQL and Redis in Docker containers
3. Start a FastAPI server and see the Swagger docs
4. Connect PyCharm's Database Tools to your containerized PostgreSQL
5. Run your first verification tests with pytest

## Step 1: Install Prerequisites

### Python 3.12 + uv

```bash
# Install uv (the fastest Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version

# uv manages Python versions too — no need for pyenv!
uv python install 3.12
```

> **ASP.NET Bridge**: `uv` is like `dotnet` CLI — it manages both the runtime AND packages. `uv sync` ≈ `dotnet restore`, `uv run` ≈ `dotnet run`.

### Node.js 20+

```bash
# If you don't have nvm yet:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# Install and use Node.js 20
nvm install 20
nvm use 20
node --version
```

### Docker Desktop

Download from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).
After installation, verify:

```bash
docker --version
docker compose version
```

## Step 2: Configure Environment

```bash
# Navigate to the project
cd /path/to/DevBrain

# Create your local environment file from the template
cp .env.example .env

# For Phase 0, the defaults work fine!
# You'll add real API keys in Phase 4.
```

## Step 3: Install Backend Dependencies

```bash
# This creates a virtual environment and installs all packages
make install-backend

# Or manually:
cd backend && uv sync
```

> **ASP.NET Bridge**: `uv sync` reads `pyproject.toml` (like `.csproj`) and `uv.lock` (like `packages.lock.json`) to install exact dependency versions.

## Step 4: Start Docker Services

```bash
# Start PostgreSQL and Redis in the background
make up

# You should see:
# ✅ Services running. PostgreSQL: localhost:5432 | Redis: localhost:6379

# Check they're running:
docker compose ps
```

## Step 5: Verify the FastAPI Server

```bash
# Start the development server
make dev-backend

# Open in your browser:
# http://localhost:8000/health  → Should show {"status": "healthy"}
# http://localhost:8000/docs    → Should show Swagger UI
```

> **ASP.NET Bridge**: The `/docs` endpoint is like Swagger/Swashbuckle in ASP.NET — but it's built into FastAPI by default. No NuGet package needed!

## Step 6: Configure PyCharm Pro

### Python Interpreter
1. Open Settings → Project → Python Interpreter
2. Click the gear icon → Add Interpreter → Add Local Interpreter
3. Select "Existing" and point to `backend/.venv/bin/python`

### Database Tools
1. Open Database tool window (View → Tool Windows → Database)
2. Click `+` → Data Source → PostgreSQL
3. Configure:
   - Host: `localhost`
   - Port: `5432`
   - User: `devbrain`
   - Password: `devbrain_secret`
   - Database: `devbrain`
4. Click "Test Connection" → should show ✅
5. You can now browse tables, run SQL queries, and inspect data directly in PyCharm!

### Docker Integration
1. Open Services tool window (View → Tool Windows → Services)
2. Click `+` → Docker Connection
3. Select "Docker for Mac"
4. You should see your running containers (devbrain-postgres, devbrain-redis)

### Recommended Plugins
Install from Settings → Plugins → Marketplace:
- ✅ Next.js Support
- ✅ Tailwind CSS
- ✅ Pydantic (if available)

## Step 7: Run Verification Tests

```bash
# Run Phase 0 verification
make verify-phase0

# Expected output: 8 tests passing
# Some Docker tests may be skipped if Docker is not running
```

## What You've Learned

| Concept | What it does | ASP.NET Equivalent |
|:--------|:-------------|:-------------------|
| `uv` | Package management | `dotnet restore` / NuGet |
| `pyproject.toml` | Project configuration | `.csproj` |
| `docker-compose.yml` | Service orchestration | None (manual install) |
| `Makefile` | Command interface | `dotnet` CLI / scripts |
| `.env` / `.env.example` | Configuration | `appsettings.json` / User Secrets |
| `FastAPI` health check | Liveness probe | `app.MapHealthChecks()` |
| `pytest` | Test runner | `dotnet test` (xUnit) |
| PyCharm Database Tools | DB inspection | SSMS / Azure Data Studio |

## Next: Phase 1 — Backend Foundation 🐍

In the next phase, you'll build the complete CRUD API with FastAPI, SQLAlchemy, and Alembic. You'll see how Controllers become Routers, Entity Framework becomes SQLAlchemy, and DTOs become Pydantic schemas.

→ See [phase-1-backend.md](phase-1-backend.md)

