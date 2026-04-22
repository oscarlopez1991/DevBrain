# Phase 1: Backend Foundation 🐍

> **Mode**: 🟡 Mixed (direct ASP.NET translation)  
> **Duration**: 1 week  
> **Prerequisites**: Phase 0 complete, Docker running (`make up`)

## Learning Objectives

By the end of this phase, you will:
1. Build a complete CRUD API with FastAPI routers
2. Define SQLAlchemy models and run Alembic migrations
3. Write Pydantic schemas for request/response validation
4. Implement a service layer separating business logic from routes
5. Pass 20 verification tests with `make verify-phase1`

## What's Provided vs What You Build

| Provided (architecture) | You implement (logic) |
|:------------------------|:----------------------|
| SQLAlchemy models & schemas | Service methods (queries) |
| Router signatures & DI wiring | Router bodies (call service, handle 404) |
| Database session management | Business logic in each service method |
| Test suite (20 tests) | The code that makes them pass |
| Alembic configuration | Running the initial migration |

## Step 1: Run the Initial Migration

Alembic is already configured. Generate and run the first migration:

```bash
# Generate migration from your models
cd backend && uv run alembic revision --autogenerate -m "initial tables"

# Or using the Makefile
make migrate-create MSG="initial tables"

# Apply the migration
make migrate
```

> **ASP.NET Bridge**: `alembic revision --autogenerate` ≈ `dotnet ef migrations add`, `alembic upgrade head` ≈ `dotnet ef database update`

Check in PyCharm Database Tools — you should see `documents` and `collections` tables.

## Step 2: Implement the Document Service

Open `backend/app/services/document_service.py`. Each method has a docstring explaining WHAT it should do. You implement the HOW.

**Files to edit:**
- `backend/app/services/document_service.py` — 5 methods to implement
- `backend/app/services/collection_service.py` — 5 methods to implement

**Key SQLAlchemy patterns you'll need:**
- `select(Model)` — Build a SELECT query
- `session.execute(stmt)` — Execute a query
- `result.scalars().all()` — Get a list of model instances
- `session.get(Model, id)` — Get by primary key
- `session.add(instance)` — Insert a new row
- `session.delete(instance)` — Delete a row
- `session.flush()` — Send pending changes to DB
- `session.refresh(instance)` — Reload from DB (get generated values)
- `model_dump(exclude_unset=True)` — Only get explicitly set fields (for partial updates)

## Step 3: Implement the Router Endpoints

Open `backend/app/api/v1/documents.py`. Each endpoint has the signature, DI wiring, and response model. You implement the body.

**Files to edit:**
- `backend/app/api/v1/documents.py` — 5 endpoints to implement
- `backend/app/api/v1/collections.py` — 5 endpoints to implement

**Pattern for each endpoint:**
1. Call the service method
2. If the service returns `None` (not found), raise `HTTPException(status_code=404)`
3. Return the result

## Step 4: Verify Your Implementation

```bash
# Run Phase 1 tests (requires Docker: make up)
make verify-phase1

# Expected: 20/20 tests passing
```

If tests fail, check:
- Is Docker running? (`docker compose ps`)
- Did you run migrations? (`make migrate`)
- Does `GET /api/v1/documents/` return `[]` (empty list) or error?

## Step 5: Explore the API

```bash
# Start the dev server
make dev-backend

# Open Swagger UI
open http://localhost:8000/docs
```

Try creating, listing, updating, and deleting documents through the Swagger UI.

## What You've Learned

| ASP.NET Concept | FastAPI Equivalent | What you did |
|:----------------|:-------------------|:-------------|
| `DbContext` | `AsyncSession` | Managed DB sessions |
| `DbSet<T>.Add()` | `session.add()` | Insert records |
| `_context.SaveChangesAsync()` | `session.flush()` + auto-commit | Persist changes |
| `EF Migrations` | Alembic | Schema versioning |
| `IRepository<T>` | Service class | Business logic layer |
| `IActionResult` → 404 | `HTTPException(404)` | Error responses |
| `[FromBody] DTO` | Pydantic schema | Request validation |

## Next: Phase 2 — Frontend Foundation 🎨

In Phase 2 you'll initialize the Next.js frontend with React, TypeScript, and Tailwind CSS.

→ See [phase-2-frontend.md](phase-2-frontend.md)
