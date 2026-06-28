# Phase 2: Frontend Foundation 🎨

> **Mode**: 🟡 Mixed (you know JS/React basics, new patterns: Next.js App Router + TypeScript)  
> **Duration**: 1 week  
> **Prerequisites**: Phase 1 complete, Node.js 20+ installed (`node --version`)

## Learning Objectives

By the end of this phase, you will:
1. Understand Next.js App Router vs traditional React SPA routing
2. Build pages with React Server Components (RSC) and Client Components
3. Use TypeScript with React props and state
4. Create a design system with Tailwind CSS v4 + shadcn/ui
5. Build a responsive sidebar layout with dark mode
6. Pass verification tests with `make verify-phase2`

## What's Provided vs What You Build

| Provided (architecture) | You implement (UI + logic) |
|:------------------------|:--------------------------|
| Next.js project scaffold | Page content and layouts |
| Tailwind + shadcn/ui config | Component composition |
| Type definitions | Props and state management |
| Sidebar shell structure | Navigation links and active states |
| Test suite | The pages/components that make them pass |

## Key Concepts: Next.js for React Developers

### App Router vs Pages Router

You may have seen React Router or even Next.js Pages Router before.
Next.js 15 uses the **App Router**, which is file-system based:

```
app/
├── layout.tsx          → Root layout (wraps ALL pages, like _app.tsx)
├── page.tsx            → Route: /
├── documents/
│   ├── page.tsx        → Route: /documents
│   └── [id]/
│       └── page.tsx    → Route: /documents/:id
└── settings/
    └── page.tsx        → Route: /settings
```

> **React SPA Bridge**: In a normal React app, you'd define routes with `<Route path="/documents" element={<Docs />} />`. In Next.js, you just create a `documents/page.tsx` file — that IS the route!

### Server Components vs Client Components

This is the biggest difference from standard React:

| | Server Component (default) | Client Component (`"use client"`) |
|:---|:---|:---|
| **Runs where** | Server only | Browser (+ server for SSR) |
| **Can use** | `async/await`, direct DB access | `useState`, `useEffect`, `onClick` |
| **When to use** | Data fetching, static content | Interactive UI, forms, animations |
| **Size impact** | Zero JS shipped to browser | JS bundle sent to browser |

> **Rule of thumb**: Everything is a Server Component by default. Only add `"use client"` when you need interactivity (clicks, inputs, state).

## Step 1: Initialize the Next.js Project

Delete the placeholder README and initialize Next.js inside the `frontend/` directory:

```bash
# Remove placeholder
rm frontend/README.md

# Initialize Next.js (non-interactive)
npx -y create-next-app@latest frontend/ \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --import-alias "@/*" \
  --use-npm
```

After initialization, verify it works:

```bash
cd frontend && npm run dev
# Open http://localhost:3000 — you should see the Next.js welcome page
```

## Step 2: Install shadcn/ui

shadcn/ui is a component library that generates the actual source code into your project
(unlike MUI or Bootstrap which are npm packages you import). This means you OWN the code
and can customize everything.

```bash
cd frontend
npx -y shadcn@latest init
```

When prompted:
- Style: **Default**
- Base color: **Neutral**
- CSS variables: **Yes**

Then install the components we need:

```bash
npx -y shadcn@latest add button card input separator
npx -y shadcn@latest add sidebar sheet tooltip
```

## Step 3: Build the Sidebar Layout

Open `frontend/app/layout.tsx`. This is the root layout that wraps every page.

**Your task**: Create a sidebar layout with navigation links:
- 📊 Dashboard (`/`)
- 📄 Documents (`/documents`)
- 🔍 Search (`/search`) — placeholder for Phase 4
- 💬 Chat (`/chat`) — placeholder for Phase 5
- ⚙️ Settings (`/settings`)

**Key files to create/edit:**
- `frontend/components/layout/app-sidebar.tsx` — The sidebar component
- `frontend/app/layout.tsx` — Wrap pages with sidebar

**Pattern (using shadcn/ui Sidebar)**:
```tsx
// components/layout/app-sidebar.tsx
"use client"

import { Sidebar, SidebarContent, SidebarMenu, SidebarMenuItem } from "@/components/ui/sidebar"
import { Home, FileText, Search, MessageSquare, Settings } from "lucide-react"

const navItems = [
  { title: "Dashboard", url: "/", icon: Home },
  { title: "Documents", url: "/documents", icon: FileText },
  { title: "Search", url: "/search", icon: Search },
  { title: "Chat", url: "/chat", icon: MessageSquare },
  { title: "Settings", url: "/settings", icon: Settings },
]

export function AppSidebar() {
  // TODO(PHASE-2): Build the sidebar navigation
  // Use shadcn/ui Sidebar components
  // Highlight the active route using usePathname()
}
```

> **React Bridge**: If you've used React Router before, `usePathname()` from `next/navigation` is like `useLocation().pathname`. It tells you which page the user is currently on.

## Step 4: Build the Dashboard Page

Open `frontend/app/page.tsx`. This is the homepage (`/`).

**Your task**: Create a dashboard with mock metric cards:
- Total Documents: 42
- Total Collections: 5
- Search Queries (today): 128
- AI Conversations: 15

**Pattern**:
```tsx
// app/page.tsx — This is a Server Component (no "use client" needed!)
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

const stats = [
  { title: "Total Documents", value: "42", icon: "📄" },
  { title: "Collections", value: "5", icon: "📁" },
  { title: "Searches Today", value: "128", icon: "🔍" },
  { title: "AI Conversations", value: "15", icon: "💬" },
]

export default function DashboardPage() {
  // TODO(PHASE-2): Render a grid of stat cards
  // Use shadcn/ui Card components
  // Make it responsive: 1 col on mobile, 2 on tablet, 4 on desktop
}
```

## Step 5: Build the Documents Page

Create `frontend/app/documents/page.tsx`.

**Your task**: Create a page that shows a list of documents (mock data for now — we'll connect to the real API in Phase 3).

**Mock data to use**:
```tsx
const mockDocuments = [
  { id: "1", title: "FastAPI Architecture", filename: "fastapi.md", status: "READY", created_at: "2026-04-28" },
  { id: "2", title: "React Patterns", filename: "react.pdf", status: "PROCESSING", created_at: "2026-04-29" },
  { id: "3", title: "Docker Guide", filename: "docker.md", status: "DRAFT", created_at: "2026-04-30" },
]
```

Use a table or card list to display them. Include a status badge with different colors for each status.

## Step 6: Dark Mode Toggle

**Your task**: Add a dark mode toggle button (usually in the sidebar footer or top-right corner).

Next.js + Tailwind v4 supports dark mode via CSS `prefers-color-scheme` or a manual class toggle.

Install the theme provider:
```bash
npm install next-themes
```

**Key pattern**:
```tsx
// components/theme-toggle.tsx
"use client"

import { useTheme } from "next-themes"
import { Button } from "@/components/ui/button"
import { Moon, Sun } from "lucide-react"

export function ThemeToggle() {
  const { theme, setTheme } = useTheme()
  // TODO(PHASE-2): Toggle between light and dark
}
```

## Step 7: Verify Your Implementation

```bash
# Run Phase 2 tests
make verify-phase2

# Expected: all tests passing
```

If tests fail, check:
- Is the dev server running? (`npm run dev`)
- Does `http://localhost:3000` load without errors?
- Are all shadcn/ui components installed?

## What You've Learned

| React SPA Concept | Next.js App Router Equivalent | What you did |
|:------------------|:-----------------------------|:-------------|
| `<BrowserRouter>` | File-system routing (`app/`) | Created pages as files |
| `<Route>` | `page.tsx` files | Each folder = a route |
| `_app.tsx` wrapper | `layout.tsx` | Root layout with sidebar |
| Everything is client | Server Components (default) | Only `"use client"` when needed |
| `useEffect` + fetch | `async` Server Components | Direct data access (Phase 3) |
| CSS-in-JS / styled | Tailwind CSS utility classes | Responsive, dark mode |

## Next: Phase 3 — Full-Stack Integration 🔌

In Phase 3 you'll connect this frontend to the FastAPI backend, fetch real data, and implement file upload.

→ See [phase-3-fullstack.md](phase-3-fullstack.md)
