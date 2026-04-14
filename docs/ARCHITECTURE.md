# DevBrain Architecture

> Technical architecture documentation for the DevBrain platform.

## System Overview

DevBrain is a document intelligence platform that uses AI to help users search, chat with, and extract insights from their document collections.

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────────────┐
│                  │     │                  │     │                          │
│   Browser/User   │────▶│   Next.js 15+    │────▶│   FastAPI Backend        │
│                  │     │   (Vercel)       │     │   (Railway)              │
│                  │     │                  │     │                          │
└──────────────────┘     └──────────────────┘     └─────────┬────────────────┘
                                                            │
                          ┌─────────────────────────────────┼─────────────┐
                          │                                 │             │
                          ▼                                 ▼             ▼
                 ┌──────────────────┐           ┌───────────────┐  ┌───────────┐
                 │   LiteLLM        │           │  PostgreSQL   │  │   Redis   │
                 │   (AI Gateway)   │           │  + pgvector   │  │  (Cache)  │
                 └────────┬─────────┘           └───────────────┘  └───────────┘
                          │
              ┌───────────┼───────────┐
              │           │           │
              ▼           ▼           ▼
     ┌──────────────┐ ┌────────┐ ┌──────────────┐
     │ Google AI    │ │  Groq  │ │ HuggingFace  │
     │ Studio       │ │        │ │ Inference    │
     │ (Primary)    │ │(Fallb.)│ │ (Fallback)   │
     └──────────────┘ └────────┘ └──────────────┘
```

## Layer Responsibilities

### Frontend (Next.js 15+ / TypeScript)
- **Server Components**: Data fetching, SEO, initial renders
- **Client Components**: Interactive UI (chat, search, file upload)
- **State Management**: Zustand for global client state
- **Styling**: Tailwind CSS v4 + shadcn/ui component library
- **Auth**: Auth.js v5 (NextAuth) with GitHub/Google OAuth

### Backend (FastAPI / Python 3.12)
- **API Layer**: RESTful endpoints with Pydantic validation
- **Service Layer**: Business logic, document processing
- **AI Layer**: LiteLLM integration, RAG pipeline, agents
- **Data Layer**: SQLAlchemy ORM + Alembic migrations
- **Task Queue**: Celery + Redis for background processing

### AI Layer (LiteLLM + LangGraph)
- **LiteLLM**: Unified API abstraction across providers
  - Primary LLM: Google AI Studio (`gemma-4-31b-it`)
  - Fallback LLM: Groq (`llama-3.3-70b-versatile`)
  - Primary Embeddings: Google AI Studio (`text-embedding-005`)
  - Fallback Embeddings: HuggingFace (`BAAI/bge-m3`)
- **LangGraph**: RAG pipeline orchestration
  - Document retrieval → Reranking → Generation
  - Agentic workflows with tool use
  - Conversation memory management

### Data Layer
- **PostgreSQL 16**: Primary relational database
  - pgvector extension for vector similarity search
  - pg_trgm extension for trigram-based text search
- **Redis**: Caching, task queue broker, rate limiting

## Key Design Decisions

### 1. Zero-Cost AI Stack
LiteLLM provides a single API surface across free-tier providers (Google AI Studio, Groq, HuggingFace). No vendor lock-in, with automatic failover.

### 2. PostgreSQL as Vector Store
Using pgvector instead of a separate vector database (Pinecone, Qdrant) simplifies the architecture. One database for relational data AND vector search.

### 3. Monorepo Structure
Frontend and backend in one repository for simpler development, shared documentation, and unified CI/CD.

### 4. SSE over WebSocket for Streaming
Server-Sent Events (SSE) is simpler than WebSocket for the unidirectional streaming we need (AI responses). Less code, easier to deploy behind reverse proxies.

## API Design

Base URL: `http://localhost:8000`

```
GET    /health                    # System health check
POST   /api/v1/documents          # Upload document
GET    /api/v1/documents          # List documents
GET    /api/v1/documents/{id}     # Get document
PUT    /api/v1/documents/{id}     # Update document
DELETE /api/v1/documents/{id}     # Delete document
POST   /api/v1/search             # Semantic search
POST   /api/v1/chat               # Chat with documents (SSE streaming)
GET    /api/v1/chat/history       # Chat history
POST   /api/v1/feedback           # Submit response feedback
GET    /api/v1/metrics            # Dashboard metrics
```

## Directory Structure

See project root `README.md` for the complete file tree.

