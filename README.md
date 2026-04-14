<!-- ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A professional README is your project's first impression. It should
  communicate what the project does, how to run it, and why it matters —
  all within the first 30 seconds of reading.

  Key elements of a portfolio-grade README:
  1. Badges (build status, license, tech stack)
  2. One-liner description
  3. Screenshot or demo GIF
  4. Quick start instructions
  5. Architecture overview
  6. Tech stack table
  7. Contributing guidelines

  Compare with ASP.NET: This is like your project's landing page in
  Visual Studio's Solution Explorer — but for the entire world to see.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ -->

<div align="center">

# 🧠 DevBrain

**AI-Powered Document Intelligence Platform**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Next.js](https://img.shields.io/badge/Next.js-15-000000?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Tailwind](https://img.shields.io/badge/Tailwind_CSS-v4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

Upload documents. Chat with them. Search semantically. Get AI-powered insights.

[Demo](#demo) · [Quick Start](#quick-start) · [Architecture](#architecture) · [Documentation](docs/ARCHITECTURE.md)

</div>

---

## ✨ Features

- 📄 **Document Processing** — Upload PDF, Markdown, and code files with automatic parsing
- 🔍 **Semantic Search** — Find documents by meaning, not just keywords, using pgvector
- 💬 **Chat with Documents** — RAG pipeline with inline citations and streaming responses
- 📊 **Dashboard** — Real-time metrics, document stats, and system health
- 🤖 **AI Agents** — Intelligent agents that search, summarize, and connect information
- 📈 **Quality Evaluation** — Systematic RAG evaluation with RAGAS framework
- 👍 **Feedback Loop** — Thumbs up/down to continuously improve AI responses
- 🔐 **Authentication** — OAuth with GitHub/Google via Auth.js v5

## 🏗️ Tech Stack

| Layer | Technology |
|:------|:-----------|
| **Frontend** | Next.js 15+, TypeScript, Tailwind CSS v4, shadcn/ui |
| **Backend** | Python 3.12, FastAPI, Pydantic v2, SQLAlchemy |
| **AI** | LiteLLM, LangGraph, Google AI Studio, Groq, HuggingFace |
| **Database** | PostgreSQL 16 + pgvector, Redis |
| **Infrastructure** | Docker Compose, GitHub Actions, Vercel, Railway |
| **Package Manager** | uv (Python), npm (Node.js) |

## 🚀 Quick Start

### Prerequisites

- [Docker Desktop](https://docker.com/products/docker-desktop) (v24+)
- [Python 3.12+](https://python.org) with [uv](https://docs.astral.sh/uv/)
- [Node.js 20+](https://nodejs.org) with npm
- [Git](https://git-scm.com)

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/devbrain.git
cd devbrain

# Copy environment variables
cp .env.example .env

# Start infrastructure (PostgreSQL + Redis)
make up

# Install backend dependencies
make install-backend

# Install frontend dependencies
make install-frontend

# Run database migrations
make migrate

# Start development servers
make dev
```

The app will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🏛️ Architecture

<!-- TODO(PHASE-8): Replace with actual architecture diagram -->
```
Browser → Next.js (Vercel) → FastAPI (Railway) → PostgreSQL + pgvector
                                    ↓
                              LiteLLM → Google AI Studio / Groq / HuggingFace
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed architecture documentation.

## 📁 Project Structure

```
DevBrain/
├── backend/          # FastAPI application (Python)
├── frontend/         # Next.js application (TypeScript)
├── docs/             # Documentation & architecture guides
├── scripts/          # Helper scripts (seeding, evaluation)
├── docker-compose.yml
├── Makefile          # Project command interface
└── .env.example      # Environment template
```

## 🧪 Testing

```bash
# Run all backend tests
make test-backend

# Run frontend tests
make test-frontend

# Run phase verification checks
make verify-phase0
make verify-phase1
# ... etc

# Run all verifications
make verify-all
```

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built with ❤️ as a Fullstack AI Engineer portfolio project</sub>
</div>

