# Frontend (Next.js)

> **Phase 2** — This directory will be initialized with Next.js in Phase 2.

## Why Not Now?

In Phase 0, we focus on infrastructure (Docker, PostgreSQL, Redis) and backend scaffolding.
The frontend will be set up in Phase 2 using:

```bash
npx -y create-next-app@latest ./  --typescript --tailwind --eslint --app --src-dir=false --import-alias="@/*"
```

## What Will Be Here

```
frontend/
├── app/                # Next.js App Router pages
│   ├── layout.tsx      # Root layout with sidebar
│   ├── page.tsx        # Dashboard
│   ├── documents/      # Document pages
│   ├── search/         # Search page
│   ├── chat/           # Chat interface
│   └── settings/       # Settings
├── components/         # React components
│   ├── ui/             # shadcn/ui components
│   ├── layout/         # Layout components
│   └── features/       # Feature-specific components
├── lib/                # Utilities, API client, types
├── hooks/              # Custom React hooks
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── Dockerfile
```

## Coming in Phase 2 🎨

See [../docs/phases/phase-2-frontend.md](../docs/phases/phase-2-frontend.md) for the full setup guide.

