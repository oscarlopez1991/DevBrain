# 🧠 DevBrain — Learning Guide

> A structured guide for transitioning from ASP.NET to Fullstack AI Engineering.

## How This Project Works

DevBrain is a **guided, incremental learning project**. You build a real, portfolio-worthy application while learning the modern AI fullstack in a structured way.

### Learning Mechanisms

#### 1. Pedagogical Comments (`LEARN:`)
Throughout the codebase, you'll find `LEARN:` blocks explaining concepts with ASP.NET comparisons:

```python
# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FastAPI routers are equivalent to ASP.NET Controllers.
# Instead of inheriting from ControllerBase...
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### 2. TODO Exercises (`TODO(PHASE-X):`)
Each phase has tasks for you to implement. They start guided and become more challenging:

```python
# TODO(PHASE-1): Implement the GET /documents endpoint
# Requirements:
# 1. Accept pagination parameters (skip, limit)
# 2. Use DocumentService (injected with Depends)
# ...
```

#### 3. Verification Tests (`CHECK:`)
Run tests to verify your implementation is correct:

```bash
make verify-phase1  # Run Phase 1 checks
```

#### 4. Challenge Exercises (`CHALLENGE:`)
Optional harder exercises for deeper learning:

```python
# CHALLENGE(PHASE-1): Add filtering by 'status' enum
```

---

## The ASP.NET → Python/React Translation Table

This is your rosetta stone. Refer back to this whenever you encounter something unfamiliar.

### Architecture Patterns

| ASP.NET Concept | Python/FastAPI Equivalent | Notes |
|:----------------|:-------------------------|:------|
| `Program.cs` + `Startup.cs` | `main.py` | App creation and configuration |
| `Controller` | `Router` | Request handling |
| `[HttpGet]`, `[HttpPost]` | `@router.get()`, `@router.post()` | Route decorators |
| `IServiceCollection` | `Depends()` | Dependency injection |
| `Entity Framework` | `SQLAlchemy` | ORM |
| `EF Migrations` | `Alembic` | Database migrations |
| `Data Annotations` / DTOs | `Pydantic` models | Validation & serialization |
| `appsettings.json` | `.env` + `Pydantic Settings` | Configuration |
| `IConfiguration` | `settings` (module-level) | Config access |
| `Middleware` | `Middleware` | Same concept! |
| `.csproj` | `pyproject.toml` | Project file |
| `NuGet` | `uv` (PyPI packages) | Package manager |
| `Kestrel` | `Uvicorn` | Web server |
| `xUnit` / `NUnit` | `pytest` | Testing framework |
| `IHostedService` | `Celery` tasks | Background jobs |
| `IDistributedCache` | `Redis` | Caching |
| `SignalR` | `SSE` (Server-Sent Events) | Real-time streaming |

### Frontend Patterns

| Razor / Blazor | Next.js / React | Notes |
|:---------------|:----------------|:------|
| Razor Pages | React Server Components | Server-rendered |
| `@model` | `props` / `params` | Component data |
| Partial Views | Components | Reusable UI pieces |
| Layout Pages | `layout.tsx` | Shared layouts |
| Tag Helpers | JSX | Template syntax |
| `ViewBag` / `ViewData` | React Context / Zustand | State management |
| CSS Isolation | Tailwind CSS / CSS Modules | Scoped styles |

---

## Learning Mode: Adaptive by Domain Distance

Difficulty is NOT linear — it adapts to how far each topic is from your ASP.NET experience:

### 🟢 Guided Mode — When the domain is NEW to you
**Applies to**: Phase 0 (setup), Phase 2 (React/Next.js), Phase 4 (AI/embeddings)
- **Every step is explained** with ASP.NET comparisons (where applicable)
- **Hints are provided** in TODOs with code examples
- **80% boilerplate is pre-generated** — you fill in the logic
- Focus: Understanding genuinely new concepts

### 🟡 Mixed Mode — When you know the CONCEPTS but not the TOOLS
**Applies to**: Phase 1 (CRUD), Phase 3 (integration), Phase 5 (RAG), Phase 6 (auth), Phase 7 (agents)
- **Architecture is explained**, implementation is on you
- **TODOs describe WHAT to build**, not step-by-step HOW
- **40% skeleton provided** — you write the core logic
- Focus: Translating your experience to new tools

### 🔴 Challenge Mode — When you should be INDEPENDENT
**Applies to**: Phase 8 (deployment)
- **Goals and acceptance criteria defined**, approach is yours
- **10% provided** — just file structure and tests
- Focus: Independence and production-grade quality

### Why this approach?

```
Phase 0 (Setup):        New ecosystem, new tools                → 🟢 Guided
Phase 1 (Backend CRUD): You already know Controllers, EF, DTOs → 🟡 Mixed
Phase 2 (React/Next.js): Components, hooks, JSX = totally new  → 🟢 Guided
Phase 3 (Full-Stack):   Connecting pieces you learned separately → 🟡 Mixed
Phase 4 (AI Embeddings): No .NET equivalent exists              → 🟢 Guided
Phase 5 (RAG Pipeline): Builds on Phase 4 foundations           → 🟡 Mixed
Phase 6 (Auth/CI):      .NET Identity concepts apply            → 🟡 Mixed
Phase 7 (Agents/Eval):  New concepts with Phase 4-5 as base    → 🟡 Mixed
Phase 8 (Deploy):       Should be independent by now            → 🔴 Challenge
```

| Phase | Topic | Distance from .NET | Mode |
|:------|:------|:-------------------|:-----|
| 0 | Setup & Environment | — | 🟢 Guided |
| 1 | Backend CRUD | **Close** | 🟡 Mixed |
| 2 | Frontend React/Next.js | **Far** | 🟢 Guided |
| 3 | Full-Stack Integration | **Medium** | 🟡 Mixed |
| 4 | AI Core (embeddings) | **Very far** | 🟢 Guided |
| 5 | RAG Pipeline | **Far** | 🟡 Mixed |
| 6 | Auth + Production | **Medium** | 🟡 Mixed |
| 7 | Agents + Evaluation | **Far** | 🟡 Mixed |
| 8 | Deploy | **Medium** | 🔴 Challenge |

---

## Recommended Learning Resources

### Python & FastAPI
- [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/) — Best tutorial for backend devs
- [SQLAlchemy 2.0 Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) — ORM patterns
- [Pydantic v2 Docs](https://docs.pydantic.dev/latest/) — Validation like a pro

### Next.js & React
- [Next.js App Router Docs](https://nextjs.org/docs/app) — The definitive guide
- [React Official Tutorial](https://react.dev/learn) — Modern React from scratch
- [Tailwind CSS v4](https://tailwindcss.com/docs) — Utility-first CSS

### AI Engineering
- [LiteLLM Docs](https://docs.litellm.ai/) — Multi-provider LLM abstraction
- [LangGraph Tutorial](https://langchain-ai.github.io/langgraph/) — LLM orchestration
- [pgvector Guide](https://github.com/pgvector/pgvector) — Vector search in PostgreSQL

### DevOps
- [Docker Compose Docs](https://docs.docker.com/compose/) — Multi-container apps
- [uv Documentation](https://docs.astral.sh/uv/) — Modern Python packaging

---

## Tips for Success

1. **Don't skip phases.** Each one builds on the previous.
2. **Run verification tests** before moving to the next phase.
3. **Read the LEARN comments** — they save you hours of confusion.
4. **Commit frequently** with conventional commit messages: `feat:`, `fix:`, `docs:`.
5. **When stuck**, check the official docs (links above) before searching Stack Overflow.
6. **Break things on purpose** — understanding errors is the fastest way to learn.

