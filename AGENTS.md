# AGENTS.md

This file provides persistent project-level instructions for coding agents working on DevBrain.

## Project

DevBrain is a full-stack AI engineering portfolio project AND a guided learning vehicle. It is a document intelligence platform (upload, semantic search, RAG chat) built incrementally across 9 phases (0–8), each with increasing autonomy.

Repository structure:
- `backend/` — FastAPI, SQLAlchemy, Alembic, Pydantic v2, pytest
- `frontend/` — Next.js 16+ App Router, TypeScript, Tailwind CSS v4, shadcn/ui
- `docs/` — architecture, implementation plan, learning guide, phase guides
- `Makefile` — unified command interface for the entire project

**Read before generating ANY code:**
- `docs/implementation_plan.md` — master plan with phases, features, and structure
- `docs/ARCHITECTURE.md` — system overview, layers, tech decisions
- `docs/LEARNING_GUIDE.md` — pedagogical rules, comment patterns, guidance levels
- `docs/PROGRESS.md` — what is complete, what is next
- `docs/phases/phase-N-*.md` — detailed guide for the phase you are generating

## Language

All code, variable names, function names, comments, docstrings, commit messages, and documentation must be in **English**. No exceptions.

## Package Managers

- Python: use `uv` / `uv run` / `uv sync`, never `pip` directly
- Frontend: use `pnpm`, never `npm` or `yarn`

## Core Commands

```
make up                — Start PostgreSQL and Redis (Docker)
make down              — Stop infrastructure
make dev-backend       — Run FastAPI dev server (uvicorn --reload)
make dev-frontend      — Run Next.js dev server (pnpm dev)
make install-backend   — Install Python deps (uv sync)
make install-frontend  — Install Node deps (pnpm install)
make migrate           — Apply Alembic migrations
make lint              — Ruff (Python) + ESLint (TypeScript)
make format            — Ruff format + Prettier
make verify-phaseN     — Run verification tests for phase N
make verify-all        — Run all phase verifications
```

---

## Code Generation Rules

### 1. Follow the Phased Structure

Every code generation task belongs to a specific phase (0–8). Before generating:
1. Read `docs/phases/phase-N-*.md` for that phase's detailed instructions.
2. Check `docs/PROGRESS.md` to confirm prerequisites are complete.
3. Generate ONLY what belongs to the current phase. Do not implement future-phase features.

### 2. Respect Guidance Levels

Each phase has a guidance mode defined in `docs/LEARNING_GUIDE.md`. Adapt the amount of pre-generated code accordingly:

| Mode | Boilerplate Provided | User Implements | Comment Depth |
|:-----|:---------------------|:----------------|:--------------|
| 🟢 **Guided** (Phases 0, 4) | ~80% scaffold + hints | Fill in core logic | Every step explained with ASP.NET comparisons |
| 🟡 **Mixed** (Phases 1, 2, 3, 5, 6, 7) | ~40% skeleton + TODOs | Write the core logic | Architecture explained, HOW is on the user |
| 🔴 **Challenge** (Phase 8) | ~10% structure + tests | Full implementation | Goals and acceptance criteria only |

**Never** generate a complete working solution in 🟡 Mixed or 🔴 Challenge mode. The user must write the core logic themselves.

### 3. Pedagogical Comment Patterns

Every generated file MUST include the appropriate comment markers as defined in `docs/LEARNING_GUIDE.md`:

#### `LEARN:` blocks — Explain concepts with ASP.NET comparisons
```python
# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# [Concept explanation with ASP.NET bridge where applicable]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### `TODO(PHASE-N):` blocks — Tasks for the user to implement
```python
# TODO(PHASE-1): [What to implement]
# Requirements:
# 1. [Specific requirement]
# 2. [Specific requirement]
#
# Hint: [Only in 🟢 Guided mode]
```

#### `CHECK(PHASE-N):` blocks — Verification instructions
```python
# CHECK(PHASE-1): Run `make verify-phase1`
# ✅ Expected: N/N tests passing
# If test_X fails, check [specific debugging guidance]
```

#### `CHALLENGE(PHASE-N):` blocks — Optional harder exercises
```python
# CHALLENGE(PHASE-1): [Description of stretch goal]
```

### 4. Verification Tests

Every phase MUST include verification tests that act as the "exam":

**Backend tests** go in: `backend/tests/verification/test_phaseN_check.py`
**Frontend tests** go in: `frontend/__tests__/verification/`

Test file structure:
```python
# tests/verification/test_phaseN_check.py
"""
╔══════════════════════════════════════════════════════════════╗
║                  VERIFICATION PHASE N                       ║
║  Run: make verify-phaseN                                    ║
║  Goal: 100% passing                                         ║
╚══════════════════════════════════════════════════════════════╝
"""

class TestPhaseN_Category:
    """Verifica [what this group tests]"""

    def test_specific_behavior(self):
        """[Human-readable description of what is being verified]"""
        ...
```

Tests must:
- Verify the user's implementation is correct, not test the scaffold itself.
- Have clear, descriptive names that tell the user what failed and why.
- Include debugging hints in the test docstrings.
- Be runnable with `make verify-phaseN`.

### 5. What to Generate per Phase

For each phase, generate these artifacts:

| Artifact | Location | Purpose |
|:---------|:---------|:--------|
| Scaffold code | `backend/app/` or `frontend/app/` | Files with `LEARN:` comments, `TODO:` blocks, and signatures |
| Verification tests | `backend/tests/verification/` or `frontend/__tests__/verification/` | Tests that pass when the user completes the TODOs |
| Phase guide (if missing) | `docs/phases/phase-N-*.md` | Step-by-step instructions with learning objectives |

### 6. Architecture Patterns

Follow the patterns defined in `docs/ARCHITECTURE.md`:

**Backend (FastAPI):**
- Routers in `app/api/v1/` — request handling only, no business logic
- Services in `app/services/` — all business logic lives here
- Models in `app/models/` — SQLAlchemy ORM models
- Schemas in `app/schemas/` — Pydantic v2 request/response schemas
- AI code in `app/ai/` — embeddings, chunking, RAG, agents
- Core utilities in `app/core/` — logging, errors, config

**Frontend (Next.js):**
- Pages in `app/` — App Router file-system routing
- Components in `components/` — `ui/` (shadcn), `layout/`, `features/`
- Utilities in `lib/` — API client, types, helpers
- Hooks in `hooks/` — custom React hooks

**Tool-specific rules** exist in `.cursor/rules/` for Cursor agents:
- `backend.mdc` — FastAPI coding conventions (glob: `backend/**/*.py`)
- `frontend.mdc` — Next.js coding conventions (glob: `frontend/**/*.{ts,tsx}`)

### 7. "Provided vs You Build" Tables

Every phase guide and scaffold MUST include a clear table showing what is pre-generated vs what the user implements. Example from Phase 1:

```markdown
| Provided (architecture) | You implement (logic) |
|:------------------------|:----------------------|
| SQLAlchemy models       | Service methods        |
| Router signatures       | Router bodies          |
| Test suite              | The code that passes   |
```

---

## Boundaries

**Ask the user first before:**
- Generating or editing Alembic migrations
- Changing the database schema (models)
- Adding new dependencies to `pyproject.toml` or `package.json`
- Generating code for a phase that is NOT the current focus

**Never:**
- Modify `.env` or commit secrets
- Edit lockfiles (`uv.lock`, `pnpm-lock.yaml`) manually
- Remove or bypass failing tests
- Generate complete solutions in 🟡 Mixed or 🔴 Challenge mode
- Skip `LEARN:` comments in 🟢 Guided or 🟡 Mixed phases
- Generate code that belongs to a future phase

## Validation

Before considering any phase generation complete:
1. Verify all generated files follow the comment patterns (`LEARN:`, `TODO:`, `CHECK:`, `CHALLENGE:`).
2. Verify the verification test file exists and covers all `TODO:` items.
3. Verify the generated code respects the guidance level (not too much, not too little).
4. Run `make verify-phaseN` mentally — the tests should FAIL until the user completes the TODOs.
5. Ensure the project starts without errors after adding the new files.