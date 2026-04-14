# DevBrain — Proyecto-Portfolio de Fullstack AI Engineer

## Contexto y Visión

Eres senior dev en ASP.NET con 2 años de gap. Ya conoces patrones MVC, REST APIs, OOP, bases de datos, y has aprendido las bases de JS. Has trabajado previamente con FastAPI (json-extractor-api) y React/Vite (SatoshiUI), así que no partes de cero.

**El objetivo**: Un proyecto-portfolio **real y desplegable** que demuestre competencia end-to-end como Fullstack AI Engineer, y que al mismo tiempo sirva como **vehículo de aprendizaje guiado e incremental**.

---

## 🎯 La Idea del Proyecto: **DevBrain**

> **Una plataforma de inteligencia documental potenciada por IA** donde los usuarios pueden subir documentos (PDF, Markdown, código), chatear con ellos usando RAG, obtener resúmenes automáticos, y buscar semánticamente en toda su base de conocimiento.

### ¿Por qué esta idea es "imbatible" para portfolio?

| Criterio | Cómo lo cumple DevBrain |
|:---|:---|
| **AI-native** | No es un CRUD con ChatGPT pegado. RAG, embeddings, vectores y agentes son el core |
| **Demuestra profundidad** | Hybrid search, reranking, streaming, evaluación con RAGAS |
| **Full-stack real** | Frontend rico (dashboard, chat, visor de documentos) + Backend robusto |
| **Tecnologías demandadas** | Next.js + TypeScript + Tailwind + FastAPI + PostgreSQL + pgvector + Docker |
| **Desplegable** | Puede funcionar en local, Docker, o cloud (Vercel + Railway/Render) |
| **Genuinamente útil** | Tú mismo podrías usarlo como tu segundo cerebro de desarrollador |
| **Diferenciador** | Incluye evaluación sistemática de IA (RAGAS), observabilidad, y feedback loop |

### Features principales (progresivas):

1. 📄 **Upload & Processing** — Subida de documentos con parsing automático (PDF, MD, code)
2. 🔍 **Semantic Search** — Búsqueda por significado usando embeddings + pgvector
3. 💬 **Chat with Docs** — RAG pipeline completo con citas inline
4. 📊 **Dashboard** — Métricas de uso, documentos, y estado del sistema
5. 🤖 **AI Agents** — Agente que puede buscar, resumir, y conectar información
6. 📈 **Evaluation** — Sistema de evaluación de calidad de respuestas (RAGAS)
7. 👍 **Feedback Loop** — Thumbs up/down con almacenamiento para mejora continua
8. 🔐 **Auth & Teams** — Autenticación y espacios de trabajo compartidos

---

## 🏗️ Stack Tecnológico Completo

```
┌──────────────────────────────────────────────────────────┐
│                      FRONTEND                            │
│  Next.js 15+ · TypeScript · Tailwind CSS v4 · shadcn/ui  │
│  React Server Components · Zustand (state)               │
└────────────────────────┬─────────────────────────────────┘
                         │ REST + SSE (streaming)
┌────────────────────────┴─────────────────────────────────┐
│                      BACKEND                             │
│  Python 3.12 · FastAPI · Pydantic v2 · SQLAlchemy        │
│  Celery (async tasks) · Redis (cache + broker)           │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────┴─────────────────────────────────┐
│                     AI LAYER (Zero Cost)                  │
│  LiteLLM (abstraction) · LangGraph (orchestration)       │
│  Google AI Studio: gemma-4-31b-it + text-embedding-005   │
│  Groq: llama-3.3-70b (fallback LLM)                     │
│  HuggingFace: BAAI/bge-m3 (fallback embeddings)         │
│  pgvector · Reranking · RAGAS (eval)                     │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────┴─────────────────────────────────┐
│                   DATA & INFRA                           │
│  PostgreSQL 16 + pgvector · Redis (Upstash) · Docker     │
│  GitHub Actions (CI/CD) · Alembic (migrations)           │
│  Deploy: Vercel (frontend) + Railway (backend + DB)      │
└──────────────────────────────────────────────────────────┘
```

---

## 📚 Fases de Aprendizaje Incremental

Cada fase se construye sobre la anterior. Cada una incluye:
- `README.md` con objetivos de aprendizaje y contexto
- Código con comentarios pedagógicos (`LEARN:`, `TODO:`, `CHECK:`, `CHALLENGE:`)
- Tests de verificación que actúan como "examen"
- Branch de Git dedicada para comparar tu solución

---

### Fase 0: Fundamentos & Entorno 🔧
**Duración estimada**: 2-3 días · **Learning Mode**: 🟢 Guided · **Razón**: Entorno nuevo, herramientas nuevas  
**Objetivo**: Configurar el entorno de desarrollo profesional

- [ ] Instalar y configurar PyCharm Pro (plugins: Next.js, Docker, Database)
- [ ] Configurar Python 3.12 con uv
- [ ] Configurar Node.js 20+ con nvm
- [ ] Crear la estructura base del monorepo
- [ ] Docker Compose con PostgreSQL + Redis
- [ ] `.env.example`, `.gitignore`, `Makefile`
- [ ] Primer `docker compose up` exitoso
- [ ] Conectar PyCharm Database Tools a PostgreSQL containerizado

**🎓 Aprenderás**: Monorepo, Docker Compose, uv package management, variables de entorno, Makefile como interfaz de proyecto

---

### Fase 1: Backend Foundation con FastAPI 🐍
**Duración estimada**: 1 semana · **Learning Mode**: 🟡 Mixed · **Razón**: CRUD es traducción directa de ASP.NET  
**Objetivo**: API REST robusta con Python moderno

- [ ] Estructura de proyecto FastAPI (routers, services, models, schemas)
- [ ] Modelos SQLAlchemy + Alembic migrations
- [ ] CRUD completo para `documents` y `collections`
- [ ] Pydantic v2 schemas con validación
- [ ] Error handling centralizado
- [ ] Health check endpoint
- [ ] Tests con pytest (unitarios + integración)

**🎓 Aprenderás**: FastAPI idiomático, SQLAlchemy async, Alembic, Pydantic v2, pytest, dependency injection  
**🔗 Puente ASP.NET**: Compararás patrones que ya conoces (Controllers→Routers, EF→SQLAlchemy, DTOs→Schemas)

---

### Fase 2: Frontend Foundation con Next.js 🎨
**Duración estimada**: 1 semana · **Learning Mode**: 🟢 Guided · **Razón**: React/Next.js = modelo mental nuevo (componentes, hooks, JSX)  
**Objetivo**: UI moderna con Next.js App Router + TypeScript

- [ ] Proyecto Next.js 15+ con App Router
- [ ] Sistema de diseño con Tailwind CSS v4 + shadcn/ui
- [ ] Layout principal con sidebar navegable
- [ ] Página de dashboard con métricas (mock data)
- [ ] Página de listado de documentos
- [ ] Components reutilizables (Button, Card, Modal, DataTable)
- [ ] Dark mode toggle
- [ ] Responsive design

**🎓 Aprenderás**: React Server Components, App Router, TypeScript en React, Tailwind CSS v4, component library  
**🔗 Puente ASP.NET**: Compararás con Razor Pages / MVC Views

---

### Fase 3: Full-Stack Integration 🔌
**Duración estimada**: 1 semana · **Learning Mode**: 🟡 Mixed · **Razón**: Conectar piezas ya aprendidas por separado  
**Objetivo**: Conectar frontend y backend end-to-end

- [ ] API client con fetch/axios + tipos TypeScript auto-generados
- [ ] Upload de archivos (drag & drop → API → storage)
- [ ] Listado real de documentos desde la API
- [ ] Estado global con Zustand
- [ ] Loading states, error boundaries, optimistic updates
- [ ] CORS, proxy config, environment management
- [ ] Docker Compose unificado (frontend + backend + DB)

**🎓 Aprenderás**: API integration patterns, state management, file upload, Docker multi-service  
**🔗 Puente ASP.NET**: Compararás con la integración tipo Blazor o API controllers

---

### Fase 4: AI Core — Embeddings & Vector Search 🧠
**Duración estimada**: 1 semana · **Learning Mode**: 🟢 Guided · **Razón**: Dominio completamente nuevo — embeddings, vectores, cosine distance no existen en .NET  
**Objetivo**: Integrar IA como ciudadano de primera clase

- [ ] Configurar pgvector en PostgreSQL
- [ ] LiteLLM setup with Google AI Studio (`text-embedding-005`)
- [ ] Fallback embeddings via HuggingFace (`BAAI/bge-m3`)
- [ ] Document chunking pipeline (semantic chunking con overlap)
- [ ] Almacenar embeddings en PostgreSQL/pgvector
- [ ] Endpoint de búsqueda semántica
- [ ] UI de búsqueda con resultados relevantes y scores
- [ ] Tests de calidad de retrieval

**🎓 Aprenderás**: Embeddings, vector databases, LiteLLM abstraction, chunking strategies, similarity search, cosine distance  
**🔗 Puente ASP.NET**: Concepto nuevo — aquí empieza tu diferenciación como AI engineer

---

### Fase 5: RAG Pipeline — Chat with Documents 💬
**Duración estimada**: 1-2 semanas · **Learning Mode**: 🟡 Mixed · **Razón**: Construye sobre Phase 4, ya tienes base AI  
**Objetivo**: Pipeline RAG completo con streaming

- [ ] LangGraph para orquestación del pipeline RAG
- [ ] LiteLLM: Google AI Studio `gemma-4-31b-it` (primary) + Groq `llama-3.3-70b` (fallback)
- [ ] Hybrid search (embeddings + BM25 keyword search)
- [ ] Reranking de resultados
- [ ] Generación con citas inline (grounded generation)
- [ ] Streaming de respuestas via SSE
- [ ] Chat UI con historial de conversación
- [ ] Gestión de contexto y memory
- [ ] Rate limiting y cost tracking

**🎓 Aprenderás**: RAG architecture, LangGraph, LiteLLM multi-provider, hybrid search, streaming, prompt engineering  
> [!IMPORTANT]
> Esta es la fase más importante para tu perfil. Un RAG bien implementado con evaluación es lo que separa a un "wrapper de ChatGPT" de un AI engineer real.

---

### Fase 6: Production Hardening 🛡️
**Duración estimada**: 1 semana · **Learning Mode**: 🟡 Mixed · **Razón**: Auth y CI/CD son conceptos conocidos de .NET, herramientas nuevas  
**Objetivo**: Convertir el proyecto en production-ready

- [ ] Autenticación (Auth.js v5 + JWT stateless con FastAPI)
- [ ] OAuth providers: GitHub + Google
- [ ] Background tasks con Celery + Redis
- [ ] Logging estructurado (structlog)
- [ ] Observabilidad básica (métricas de retrieval, latencia, costes)
- [ ] Error tracking
- [ ] Rate limiting por usuario
- [ ] Tests E2E con Playwright
- [ ] CI/CD con GitHub Actions (lint, test, build, deploy)

**🎓 Aprenderás**: Auth.js v5 patterns, JWT stateless, async tasks, observability, CI/CD, E2E testing

---

### Fase 7: Advanced AI — Agents & Evaluation 🤖
**Duración estimada**: 1-2 semanas · **Learning Mode**: 🟡 Mixed · **Razón**: Conceptos nuevos (agents, eval) pero ya tienes base AI de Phase 4-5  
**Objetivo**: Features avanzadas que demuestran profundidad

- [ ] Agente AI con herramientas (search, summarize, compare docs)
- [ ] Evaluación sistemática con RAGAS (Faithfulness, Relevance, Context Precision)
- [ ] Golden dataset (50+ pares Q&A ground truth)
- [ ] Dashboard de evaluación de calidad
- [ ] User feedback (thumbs up/down) con storage
- [ ] LiteLLM multi-provider failover (Google → Groq → HF)
- [ ] Stress testing del pipeline RAG

**🎓 Aprenderás**: AI agents, tool use, evaluation frameworks, feedback loops, LiteLLM multi-provider failover

---

### Fase 8: Deployment & Portfolio Presentation 🚀
**Duración estimada**: 3-5 días · **Learning Mode**: 🔴 Challenge · **Razón**: Ya deberías ser independiente, Vercel/Railway son simples  
**Objetivo**: Desplegar y presentar profesionalmente

- [ ] Deploy del frontend en Vercel
- [ ] Deploy del backend en Railway
- [ ] PostgreSQL + pgvector on Railway
- [ ] Redis on Upstash (LiteLLM request caching)
- [ ] README profesional con badges, arquitectura, screenshots, demo GIF
- [ ] Landing page del proyecto (en el propio Next.js)
- [ ] Documentación de API (auto-generated con FastAPI)
- [ ] Blog post / case study sobre decisiones técnicas
- [ ] No vendor-locked cloud SDKs (no AWS S3/Bedrock, no GCP Vertex)

**🎓 Aprenderás**: Cloud deployment, managed databases, technical writing, portfolio presentation

---

## 📝 Mecanismos de Aprendizaje

### Sistema de Comentarios Pedagógicos

```python
# ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# En FastAPI, los "routers" son el equivalente a los Controllers
# de ASP.NET. En lugar de heredar de ControllerBase, defines 
# funciones decoradas con @router.get(), @router.post(), etc.
# 
# Diferencia clave vs ASP.NET:
# - No hay clases Controller, son funciones puras
# - Dependency Injection funciona con Depends() en los parámetros
# - Los tipos de retorno se validan con Pydantic (similar a DTOs)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

router = APIRouter(prefix="/documents", tags=["documents"])


# TODO(FASE-1): Implementa el endpoint GET /documents
# Requisitos:
# 1. Acepta parámetros de paginación (skip, limit) con valores por defecto
# 2. Usa el servicio DocumentService (inyectado con Depends)
# 3. Retorna una lista de DocumentResponse (el schema Pydantic)
# 4. Maneja el caso de colección vacía (200 con lista vacía, NO 404)
#
# Pista: Mira cómo funciona Depends() — es como el DI container 
# de ASP.NET pero declarativo en los parámetros de la función.
@router.get("/", response_model=list[DocumentResponse])
async def list_documents(
    # Tu código aquí
    ...
):
    pass


# CHECK(FASE-1): Ejecuta `pytest tests/test_documents.py -v`
# ✅ Deberías ver 5/5 tests passing
# Si falla test_list_documents_empty, revisa que retornas [] y no None
# Si falla test_list_documents_pagination, revisa skip/limit defaults


# CHALLENGE(FASE-1): Añade un parámetro de filtrado por 'status'
# que acepte un Enum (draft, processing, ready, error)
# Extra: Haz que sea opcional y que sin filtro devuelva todos
```

```typescript
// ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// React Server Components (RSC) son componentes que se ejecutan
// SOLO en el servidor. Es como si Razor Pages y React tuvieran
// un hijo: obtienes el rendering del servidor con la composición 
// de React.
//
// Regla de oro: Si no necesita interactividad (clicks, inputs, 
// estado), déjalo como Server Component. Solo añade "use client"
// cuando necesites hooks (useState, useEffect, etc.)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

// TODO(FASE-2): Este componente muestra la lista de documentos
// Como es un Server Component, puedes hacer fetch directamente aquí
// sin useEffect ni useState. El fetch se ejecuta en el servidor.
//
// Implementa:
// 1. Fetch a GET /api/documents (usa la URL del backend)  
// 2. Renderiza cada documento en un <DocumentCard />
// 3. Maneja el estado de carga con <Suspense>
// 4. Maneja errores con una boundary
export default async function DocumentsPage() {
  // Tu código aquí
}

// CHECK(FASE-2): Abre http://localhost:3000/documents
// ✅ Deberías ver los documentos cargados desde la API
// ✅ El layout debería ser un grid responsive (1 col mobile, 3 desktop)
// ❌ Si ves "loading..." infinito, revisa la URL de la API
```

### Tests como Sistema de Verificación

```python
# tests/verification/test_fase1_check.py
"""
╔══════════════════════════════════════════════════════════════╗
║                  VERIFICACIÓN FASE 1                        ║
║  Ejecuta estos tests para confirmar que has completado      ║
║  correctamente la Fase 1: Backend Foundation                ║
║                                                             ║
║  Comando: pytest tests/verification/test_fase1_check.py -v  ║
║  Meta: 100% passing (12/12 tests)                           ║
╚══════════════════════════════════════════════════════════════╝
"""

class TestFase1_DatabaseSetup:
    """Verifica que la DB está configurada correctamente"""
    
    def test_database_connection(self):
        """¿Puedes conectarte a PostgreSQL?"""
        ...
    
    def test_tables_exist(self):
        """¿Se crearon las tablas con Alembic?"""
        ...
    
    def test_migration_is_current(self):
        """¿Están las migraciones al día?"""
        ...

class TestFase1_APIEndpoints:
    """Verifica que los endpoints CRUD funcionan"""
    
    def test_health_check(self):
        """GET /health retorna 200"""
        ...
    
    def test_create_document(self):
        """POST /documents crea un documento"""
        ...
    
    def test_list_documents(self):
        """GET /documents retorna lista"""
        ...
    
    # ... más tests
```

### Archivo PROGRESS.md de Tracking

```markdown
# 🧠 DevBrain — Tu Progreso

## Fase 0: Fundamentos & Entorno
- [x] Docker Compose funcionando
- [x] PyCharm configurado
- [ ] ...

## Fase 1: Backend Foundation  
- [ ] Estructura del proyecto creada
- [ ] Modelos SQLAlchemy definidos
- [ ] Verificación: `pytest tests/verification/test_fase1_check.py` → _/12 passing

## Fase 2: Frontend Foundation
- [ ] Next.js inicializado
- [ ] Verificación: `npm run test:fase2` → _/8 passing
...
```

---

## 📁 Estructura del Monorepo

```
DevBrain/
├── 📄 README.md                    # README profesional del proyecto
├── 📄 LICENSE                      # MIT License
├── 📄 docker-compose.yml           # Orquestación de servicios
├── 📄 docker-compose.dev.yml       # Override para desarrollo
├── 📄 Makefile                     # Interfaz de comandos del proyecto
├── 📄 .env.example                 # Plantilla de variables de entorno
├── 📄 .gitignore
│
├── 📂 backend/                     # FastAPI application
│   ├── 📄 Dockerfile
│   ├── 📄 pyproject.toml           # Dependencies (uv)
│   ├── 📄 alembic.ini
│   ├── 📂 alembic/                 # Migraciones de DB
│   ├── 📂 app/
│   │   ├── 📄 main.py              # Entry point FastAPI
│   │   ├── 📄 config.py            # Settings con Pydantic
│   │   ├── 📄 dependencies.py      # DI helpers
│   │   ├── 📂 api/                 # Routers (≈ Controllers)
│   │   │   ├── 📂 v1/
│   │   │   │   ├── 📄 documents.py
│   │   │   │   ├── 📄 search.py
│   │   │   │   ├── 📄 chat.py
│   │   │   │   └── 📄 auth.py
│   │   ├── 📂 models/              # SQLAlchemy models (≈ EF Entities)
│   │   ├── 📂 schemas/             # Pydantic schemas (≈ DTOs)
│   │   ├── 📂 services/            # Business logic (≈ Services)
│   │   ├── 📂 ai/                  # AI-specific code
│   │   │   ├── 📄 embeddings.py
│   │   │   ├── 📄 chunking.py
│   │   │   ├── 📄 rag_pipeline.py
│   │   │   ├── 📄 agents.py
│   │   │   └── 📄 evaluation.py
│   │   └── 📂 core/                # Cross-cutting (logging, errors)
│   └── 📂 tests/
│       ├── 📂 unit/
│       ├── 📂 integration/
│       └── 📂 verification/        # Tests de verificación por fase
│           ├── 📄 test_fase0_check.py
│           ├── 📄 test_fase1_check.py
│           ├── ...
│           └── 📄 test_fase7_check.py
│
├── 📂 frontend/                    # Next.js application
│   ├── 📄 Dockerfile
│   ├── 📄 package.json
│   ├── 📄 tsconfig.json
│   ├── 📄 tailwind.config.ts
│   ├── 📂 app/                     # App Router pages
│   │   ├── 📄 layout.tsx           # Root layout
│   │   ├── 📄 page.tsx             # Landing / Dashboard
│   │   ├── 📂 documents/
│   │   ├── 📂 search/
│   │   ├── 📂 chat/
│   │   └── 📂 settings/
│   ├── 📂 components/              # React components
│   │   ├── 📂 ui/                  # shadcn/ui components
│   │   ├── 📂 layout/              # Layout components
│   │   └── 📂 features/            # Feature-specific components
│   ├── 📂 lib/                     # Utilities, API client, types
│   ├── 📂 hooks/                   # Custom React hooks
│   └── 📂 __tests__/               # Frontend tests
│       └── 📂 verification/
│
├── 📂 docs/                        # Documentación adicional
│   ├── 📄 ARCHITECTURE.md
│   ├── 📄 PROGRESS.md              # Tu tracking de aprendizaje
│   ├── 📄 LEARNING_GUIDE.md        # Guía pedagógica general
│   ├── 📄 implementation_plan.md   # Plan maestro del proyecto
│   ├── 📄 API.md
│   ├── 📂 phases/                  # Guía detallada por fase
│   │   ├── 📄 phase-0-setup.md
│   │   ├── 📄 phase-1-backend.md
│   │   └── ...
│   └── 📂 diagrams/                # Diagramas de arquitectura
│
└── 📂 scripts/                     # Helper scripts
    ├── 📄 seed_db.py               # Datos de ejemplo
    ├── 📄 generate_types.sh        # Auto-gen TypeScript types
    └── 📄 evaluate_rag.py          # Script de evaluación
```

---

## 🛠️ Configuración de PyCharm Pro

### Plugins recomendados
| Plugin | Para qué |
|:---|:---|
| **Next.js Support** | Autocompletado, routing, run configs |
| **Docker** | Gestión de contenedores desde Services |
| **Database Tools** | Conexión directa a PostgreSQL containerizado |
| **Tailwind CSS** | Autocompletado de clases |
| **Pydantic** | Soporte mejorado para schemas |

### Configuración clave
1. **Remote Python Interpreter** → Apuntando al container Docker del backend
2. **Run Configurations** → FastAPI (backend), Next.js dev (frontend), Docker Compose (full stack)
3. **Database Tool Window** → Conectada a PostgreSQL en `localhost:5432`
4. **Terminal** → Con `docker compose` path configurado
5. **File Watchers** → Para auto-format con Black (Python) y Prettier (TS)

---

## ✅ Decisions Made

### 1. 🤖 AI Provider & Abstraction Layer (100% Free Stack)
| Role | Provider | Model |
|:---|:---|:---|
| **Primary LLM** | Google AI Studio | `gemma-4-31b-it` |
| **Primary Embeddings** | Google AI Studio | `text-embedding-005` |
| **Fallback LLM** | Groq | `llama-3.3-70b-versatile` / `llama-4-scout` |
| **Fallback Embeddings** | HuggingFace Inference API | `BAAI/bge-m3` |
| **Abstraction Engine** | LiteLLM | Multi-provider routing + caching |

### 2. ⏰ Dedication: 10-15 hours/week → ~16-20 weeks
Bi-weekly sprints with clear deliverables per phase.

### 3. 🔐 Auth: Auth.js v5 (NextAuth.js)
- OAuth only: GitHub + Google
- Stateless JWT strategy
- Secure API route protection for LLM requests

### 4. 🚀 Deployment: Vercel + Railway
| Service | Platform |
|:---|:---|
| Frontend | Vercel |
| Backend + DB | Railway |
| PostgreSQL + pgvector | Railway |
| Redis (cache) | Upstash or Railway native |
| **No vendor lock-in** | No AWS/GCP specific SDKs |

### 5. 📦 Python: uv exclusively
- `uv pip` and `uv sync` for reproducible environments
- Strict `uv.lock` compliance — no `requirements.txt` or `poetry.lock`

### 6. 📝 Learning Mode: Adaptive (by domain distance)
Difficulty adapts to how far each topic is from your ASP.NET experience:

| Phase | Topic | Distance from .NET | Mode | Rationale |
|:---|:---|:---|:---|:---|
| 0 | Setup & Environment | — | 🟢 Guided | New tools, new ecosystem |
| 1 | Backend CRUD | **Close** | 🟡 Mixed | Direct ASP.NET translation |
| 2 | Frontend React/Next.js | **Far** | 🟢 Guided | New mental model (components, hooks) |
| 3 | Full-Stack Integration | **Medium** | 🟡 Mixed | Connecting already-learned pieces |
| 4 | AI Core (embeddings) | **Very far** | 🟢 Guided | Entirely new domain, no .NET equivalent |
| 5 | RAG Pipeline | **Far** | 🟡 Mixed | Building on Phase 4 foundations |
| 6 | Auth + Production | **Medium** | 🟡 Mixed | .NET Identity concepts apply, new tools |
| 7 | Agents + Evaluation | **Far** | 🟡 Mixed | New concepts with Phase 4-5 as base |
| 8 | Deploy | **Medium** | 🔴 Challenge | Should be independent by now |

### 7. 🌐 Language Standard
All code (functions, variables), comments, and technical documentation **strictly in English**.

---

## Verification Plan

### Automated Tests
Cada fase tiene su suite de verificación:
```bash
# Verificar fase 0 (setup)
make verify-fase0

# Verificar fase 1 (backend)
make verify-fase1

# Verificar todo hasta la fase actual
make verify-all

# Linting y formatting
make lint
make format
```

### Manual Verification
- Cada fase incluye un checklist visual en `PROGRESS.md`
- Capturas de pantalla esperadas en `docs/phases/` para comparar tu UI
- El `README.md` final se evaluará contra un checklist de "portfolio-ready"

### Portfolio Quality Checklist (Fase 8)
- [ ] README con badges, arquitectura, screenshots, demo GIF
- [ ] API documentada con Swagger/OpenAPI auto-generado
- [ ] CI/CD pipeline verde
- [ ] Deploy funcional con URL pública
- [ ] Evaluación RAGAS con métricas reales
- [ ] Clean commit history con conventional commits
