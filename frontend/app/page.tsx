// ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Dashboard Home page component (RSC)
//
// Because this page is a Server Component, it renders server-side and has zero impact
// on the client JS bundle. It represents the route `/`.
//
// In React/Tailwind, we build responsive grids using the `grid` class and column
// specifications (e.g. `grid-cols-1 md:grid-cols-2 lg:grid-cols-4`).
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

const stats = [
  { title: "Total Documents", value: "42", icon: "📄", description: "All uploaded document files" },
  { title: "Collections", value: "5", icon: "📁", description: "Logical groupings of sources" },
  { title: "Searches Today", value: "128", icon: "🔍", description: "Semantic search queries run today" },
  { title: "AI Conversations", value: "15", icon: "💬", description: "RAG chat sessions initiated" },
]

export default function DashboardPage() {
  return (
    <div className="flex-1 space-y-4 p-8 pt-6">
      <div className="flex items-center justify-between space-y-2">
        <h2 className="text-3xl font-bold tracking-tight">Dashboard</h2>
        <p className="text-muted-foreground">Welcome back to DevBrain. Here is your knowledge overview.</p>
      </div>
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map(item => (
            <Card key={item.title}>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  {item.icon}
                  <span>{item.title}</span>
                </CardTitle>
              </CardHeader>

              <CardContent className="space-y-1">
                <div className="text-2xl font-bold tracking-tight tabular-nums">
                  {item.value}
                </div>
                <p className="text-sm text-muted-foreground">
                  {item.description}
                </p>
              </CardContent>
            </Card>
        ))}
      </div>
    </div>
  )
}

// CHECK(PHASE-2): Open http://localhost:3000 in your browser.
// ✅ Verify that all 4 stat cards render correctly with correct titles and counts.
// ✅ Resize the browser window to verify the grid columns scale from 1 on mobile to 4 on large screens.

// CHALLENGE(PHASE-2): Add a "Recent Activities" section below the metrics displaying a mock list of recently uploaded files.

