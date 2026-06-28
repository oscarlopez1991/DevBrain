# 🧠 DevBrain — Learning Progress Tracker

> Track your journey from ASP.NET developer to Fullstack AI Engineer.
> Mark items as you complete them. Run verification tests to confirm.

---

## Phase 0: Foundations & Environment 🔧 ✅ COMPLETE
**Mode**: 🟢 Guided (new tools) | **Est. Duration**: 2-3 days

### Environment Setup
- [x] Python 3.12 installed and available via `python3 --version`
- [x] uv installed and available via `uv --version`
- [x] Node.js 20+ installed via `node --version`
- [x] Docker Desktop installed and running
- [x] PyCharm Pro opened with the DevBrain project

### PyCharm Configuration
- [x] Next.js Support plugin installed
- [x] Docker plugin enabled
- [x] Database Tools plugin enabled
- [x] Tailwind CSS plugin installed
- [x] Pydantic plugin installed
- [x] Python interpreter configured (local venv via uv)

### Project Setup
- [x] `.env` file created from `.env.example`
- [x] Backend dependencies installed: `make install-backend`
- [x] Docker services running: `make up`
- [x] PostgreSQL reachable: PyCharm Database Tools connected
- [x] Redis reachable: `docker compose exec redis redis-cli ping` → PONG
- [x] FastAPI health check: http://localhost:8000/health → `{"status": "healthy"}`
- [x] Swagger UI visible: http://localhost:8000/docs

### ✅ Verification
```bash
make verify-phase0
```
- [x] Result: 8 / 8 tests passing

---

## Phase 1: Backend Foundation 🐍 ✅ COMPLETE
**Mode**: 🟡 Mixed (direct ASP.NET translation) | **Est. Duration**: 1 week

### Database & Models
- [x] Alembic initialized and configured
- [x] `Document` model created with SQLAlchemy
- [x] `Collection` model created with SQLAlchemy
- [x] Initial migration generated and applied
- [x] Seed data script working

### API Endpoints
- [x] `POST /api/v1/documents` — Create document
- [x] `GET /api/v1/documents` — List documents (with pagination)
- [x] `GET /api/v1/documents/{id}` — Get single document
- [x] `PATCH /api/v1/documents/{id}` — Update document
- [x] `DELETE /api/v1/documents/{id}` — Delete document
- [x] Collections CRUD endpoints

### Code Quality
- [x] Pydantic schemas for all models
- [x] Centralized error handling
- [x] `ruff check .` passes with no errors
- [x] `mypy .` passes with no errors

### ✅ Verification
```bash
make verify-phase1
```
- [x] Result: 20 / 20 tests passing

---

## Phase 2: Frontend Foundation 🎨
**Mode**: 🟡 Mixed (you know JS/React, new: Next.js App Router + TS) | **Est. Duration**: 1 week

### Project Setup
- [ ] Next.js 15+ initialized with App Router
- [ ] Tailwind CSS v4 configured
- [ ] shadcn/ui installed and configured
- [ ] TypeScript strict mode enabled

### Pages & Components
- [ ] Root layout with sidebar navigation
- [ ] Dashboard page with mock metrics
- [ ] Documents list page
- [ ] Reusable components: Button, Card, Modal, DataTable
- [ ] Dark mode toggle working
- [ ] Responsive on mobile/tablet/desktop

### ✅ Verification
```bash
make verify-phase2
```
- [ ] Result: ___ / 8 tests passing

---

## Phase 3: Full-Stack Integration 🔌
**Mode**: 🟡 Mixed (connecting learned pieces) | **Est. Duration**: 1 week

- [ ] API client with TypeScript types
- [ ] File upload (drag & drop → API → storage)
- [ ] Real document listing from API
- [ ] Global state management with Zustand
- [ ] Loading states and error boundaries
- [ ] Docker Compose with all services unified

### ✅ Verification
```bash
make verify-phase3
```
- [ ] Result: ___ / ___ tests passing

---

## Phase 4: AI Core — Embeddings & Vector Search 🧠
**Mode**: 🟢 Guided (entirely new domain) | **Est. Duration**: 1 week

- [ ] pgvector configured and working
- [ ] LiteLLM configured with Google AI Studio
- [ ] Embedding service with `text-embedding-005`
- [ ] Fallback to HuggingFace `BAAI/bge-m3`
- [ ] Document chunking pipeline
- [ ] Embeddings stored in pgvector
- [ ] Semantic search endpoint working
- [ ] Search UI with relevance scores

### ✅ Verification
```bash
make verify-phase4
```
- [ ] Result: ___ / ___ tests passing

---

## Phase 5: RAG Pipeline — Chat with Documents 💬
**Mode**: 🟡 Mixed (builds on Phase 4 base) | **Est. Duration**: 1-2 weeks

- [ ] LangGraph RAG pipeline
- [ ] LiteLLM with gemma-4-31b-it (primary)
- [ ] Groq llama-3.3-70b fallback
- [ ] Hybrid search (embeddings + BM25)
- [ ] Reranking
- [ ] Streaming via SSE
- [ ] Chat UI with conversation history
- [ ] Inline citations in responses

### ✅ Verification
```bash
make verify-phase5
```
- [ ] Result: ___ / ___ tests passing

---

## Phase 6: Production Hardening 🛡️
**Mode**: 🟡 Mixed (known concepts, new tools) | **Est. Duration**: 1 week

- [ ] Auth.js v5 with GitHub + Google OAuth
- [ ] JWT stateless auth for API
- [ ] Celery background tasks
- [ ] Structured logging with structlog
- [ ] Rate limiting per user
- [ ] E2E tests with Playwright
- [ ] CI/CD with GitHub Actions

### ✅ Verification
```bash
make verify-phase6
```
- [ ] Result: ___ / ___ tests passing

---

## Phase 7: Advanced AI — Agents & Evaluation 🤖
**Mode**: 🟡 Mixed (new concepts with AI base) | **Est. Duration**: 1-2 weeks

- [ ] AI agent with tools (search, summarize, compare)
- [ ] RAGAS evaluation framework
- [ ] Golden dataset (50+ Q&A pairs)
- [ ] Evaluation dashboard
- [ ] User feedback (thumbs up/down)
- [ ] LiteLLM multi-provider failover
- [ ] Stress testing pipeline

### ✅ Verification
```bash
make verify-phase7
```
- [ ] Result: ___ / ___ tests passing

---

## Phase 8: Deployment & Portfolio 🚀
**Mode**: 🔴 Challenge (independent by now) | **Est. Duration**: 3-5 days

- [ ] Frontend deployed on Vercel
- [ ] Backend deployed on Railway
- [ ] PostgreSQL + pgvector on Railway
- [ ] Redis on Upstash
- [ ] Professional README with demo GIF
- [ ] Landing page
- [ ] API documentation
- [ ] Blog post / case study

### Portfolio Quality Checklist
- [ ] Clean commit history (conventional commits)
- [ ] CI/CD pipeline green
- [ ] Live demo URL working
- [ ] README has badges, architecture diagram, screenshots
- [ ] RAGAS evaluation with real metrics
- [ ] No hardcoded secrets in code

