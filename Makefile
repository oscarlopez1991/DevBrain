# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Makefile: The Project Command Interface
#
# A Makefile provides a unified, discoverable interface for ALL project
# commands. Instead of remembering dozens of docker, pytest, npm commands,
# you just type `make <target>`.
#
# Why use a Makefile instead of scripts?
# 1. Self-documenting — `make help` shows all available commands
# 2. Dependency-aware — targets can depend on other targets
# 3. Universal — works on macOS, Linux, and WSL
# 4. Standard — most open-source projects use Makefiles
#
# Compare with ASP.NET: This replaces the "dotnet run", "dotnet test",
# "dotnet ef" commands you're used to. Instead of `dotnet ef database update`,
# you'd run `make migrate`.
#
# Usage:
#   make help          — Show all available commands
#   make up            — Start all Docker services
#   make dev           — Start development servers
#   make test          — Run all tests
#   make verify-phase0 — Verify Phase 0 completion
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# .PHONY tells Make that these targets don't correspond to actual files.
# Without this, Make would look for a file called "help" or "up" and
# skip the command if the file exists.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.PHONY: help up down dev install-backend install-frontend migrate \
        test test-backend test-frontend lint format \
        verify-phase0 verify-phase1 verify-phase2 verify-phase3 \
        verify-phase4 verify-phase5 verify-phase6 verify-phase7 \
        verify-all clean logs

# Default target — runs when you just type `make`
.DEFAULT_GOAL := help

# ──────────────────────────────────────────────────────────────
# Variables
# ──────────────────────────────────────────────────────────────
DOCKER_COMPOSE = docker compose
BACKEND_DIR = backend
FRONTEND_DIR = frontend

# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# The `help` target below uses a clever grep pattern to auto-generate
# documentation from comments in this file. Any line with `## ` after
# the target name becomes the help text.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ──────────────────────────────────────────────────────────────
# 📋 Help
# ──────────────────────────────────────────────────────────────
help: ## Show this help message
	@echo ""
	@echo "🧠 DevBrain — Project Commands"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ──────────────────────────────────────────────────────────────
# 🐳 Docker / Infrastructure
# ──────────────────────────────────────────────────────────────
up: ## Start all Docker services (PostgreSQL, Redis)
	$(DOCKER_COMPOSE) up -d
	@echo "✅ Services running. PostgreSQL: localhost:5432 | Redis: localhost:6379"

down: ## Stop all Docker services
	$(DOCKER_COMPOSE) down
	@echo "🛑 All services stopped."

down-clean: ## Stop services and remove volumes (⚠️ deletes data)
	$(DOCKER_COMPOSE) down -v
	@echo "🧹 Services stopped and volumes removed."

logs: ## Tail Docker service logs
	$(DOCKER_COMPOSE) logs -f

# ──────────────────────────────────────────────────────────────
# 📦 Dependencies
# ──────────────────────────────────────────────────────────────
install-backend: ## Install Python dependencies with uv
	cd $(BACKEND_DIR) && uv sync
	@echo "✅ Backend dependencies installed."

install-frontend: ## Install Node.js dependencies
	cd $(FRONTEND_DIR) && npm install
	@echo "✅ Frontend dependencies installed."

install: install-backend install-frontend ## Install all dependencies

# ──────────────────────────────────────────────────────────────
# 🚀 Development
# ──────────────────────────────────────────────────────────────
dev-backend: ## Start FastAPI dev server
	cd $(BACKEND_DIR) && uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-frontend: ## Start Next.js dev server
	cd $(FRONTEND_DIR) && npm run dev

dev: ## Start all development servers (requires tmux or run in separate terminals)
	@echo "🚀 Start each server in a separate terminal:"
	@echo "  Terminal 1: make dev-backend"
	@echo "  Terminal 2: make dev-frontend"
	@echo ""
	@echo "Or start infrastructure first: make up"

# ──────────────────────────────────────────────────────────────
# 🗄️ Database
# ──────────────────────────────────────────────────────────────
migrate: ## Run database migrations (Alembic)
	cd $(BACKEND_DIR) && uv run alembic upgrade head
	@echo "✅ Migrations applied."

migrate-create: ## Create a new migration (usage: make migrate-create MSG="add users table")
	cd $(BACKEND_DIR) && uv run alembic revision --autogenerate -m "$(MSG)"
	@echo "✅ Migration created. Review it in backend/alembic/versions/"

migrate-rollback: ## Rollback last migration
	cd $(BACKEND_DIR) && uv run alembic downgrade -1
	@echo "⬅️ Rolled back one migration."

# ──────────────────────────────────────────────────────────────
# 🧪 Testing
# ──────────────────────────────────────────────────────────────
test-backend: ## Run backend tests
	cd $(BACKEND_DIR) && uv run pytest -v

test-frontend: ## Run frontend tests
	cd $(FRONTEND_DIR) && npm test

test: test-backend ## Run all tests

# ──────────────────────────────────────────────────────────────
# ✅ Phase Verification
# These commands run the verification test suites for each
# learning phase. Pass all tests to confirm phase completion.
# ──────────────────────────────────────────────────────────────
verify-phase0: ## Verify Phase 0: Environment & Setup
	cd $(BACKEND_DIR) && uv run pytest tests/verification/test_phase0_check.py -v
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "✅ Phase 0 verification complete!"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

verify-phase1: ## Verify Phase 1: Backend Foundation
	cd $(BACKEND_DIR) && uv run pytest tests/verification/test_phase1_check.py -v

verify-phase2: ## Verify Phase 2: Frontend Foundation
	cd $(FRONTEND_DIR) && npm run test:phase2

verify-phase3: ## Verify Phase 3: Full-Stack Integration
	cd $(BACKEND_DIR) && uv run pytest tests/verification/test_phase3_check.py -v

verify-phase4: ## Verify Phase 4: AI Core
	cd $(BACKEND_DIR) && uv run pytest tests/verification/test_phase4_check.py -v

verify-phase5: ## Verify Phase 5: RAG Pipeline
	cd $(BACKEND_DIR) && uv run pytest tests/verification/test_phase5_check.py -v

verify-phase6: ## Verify Phase 6: Production Hardening
	cd $(BACKEND_DIR) && uv run pytest tests/verification/test_phase6_check.py -v

verify-phase7: ## Verify Phase 7: Advanced AI
	cd $(BACKEND_DIR) && uv run pytest tests/verification/test_phase7_check.py -v

verify-all: ## Run all phase verifications
	@echo "Running all phase verifications..."
	cd $(BACKEND_DIR) && uv run pytest tests/verification/ -v

# ──────────────────────────────────────────────────────────────
# 🧹 Code Quality
# ──────────────────────────────────────────────────────────────
lint: ## Run linters (ruff for Python, eslint for TypeScript)
	cd $(BACKEND_DIR) && uv run ruff check .
	cd $(FRONTEND_DIR) && npm run lint

format: ## Auto-format code (ruff for Python, prettier for TypeScript)
	cd $(BACKEND_DIR) && uv run ruff format .
	cd $(FRONTEND_DIR) && npx prettier --write "**/*.{ts,tsx,js,jsx,json,css,md}"

# ──────────────────────────────────────────────────────────────
# 🧹 Cleanup
# ──────────────────────────────────────────────────────────────
clean: ## Remove build artifacts, caches, and temp files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".next" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null || true
	@echo "🧹 All caches and artifacts cleaned."

