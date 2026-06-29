// ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Next.js App Router Page component
//
// In ASP.NET MVC, a route `/documents` would match a `DocumentsController.Index()` action,
// which returns a Razor View.
// In Next.js, this matches the file `app/documents/page.tsx`.
//
// Because this page is a Server Component by default, you can retrieve data directly
// inside the function without needing useState or useEffect, just like returning model data
// to an ASP.NET view.
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

const mockDocuments = [
  { id: "1", title: "FastAPI Architecture", filename: "fastapi.md", status: "READY", created_at: "2026-04-28" },
  { id: "2", title: "React Patterns", filename: "react.pdf", status: "PROCESSING", created_at: "2026-04-29" },
  { id: "3", title: "Docker Guide", filename: "docker.md", status: "DRAFT", created_at: "2026-04-30" },
]

export default function DocumentsPage() {
  return (
    <div className="flex-1 space-y-4 p-8 pt-6">
      <div className="flex items-center justify-between space-y-2">
        <h2 className="text-3xl font-bold tracking-tight">Documents</h2>
        <p className="text-muted-foreground">Manage your documents and process them with AI.</p>
      </div>

      <div className="grid gap-4 md:grid-cols-1">
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>All Documents</CardTitle>
            <CardDescription>
              A list of all your document sources and their current processing status.
            </CardDescription>
          </CardHeader>
          <CardContent>
            {/* TODO(PHASE-2): Render a table or card list to display the `mockDocuments`.
                Requirements:
                1. Loop through `mockDocuments` array.
                2. Show the title, filename, status, and creation date of each document.
                3. Color-code the status badges:
                   - READY: green/success
                   - PROCESSING: yellow/primary
                   - DRAFT: gray/muted
                
                Pista: You can build a custom badge or use conditional styling with inline classes.
            */}
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

// CHECK(PHASE-2): Navigate to /documents.
// ✅ Verify that all mock documents are rendered in a clean table format.
// ✅ Verify that the status badges are correctly styled and colored.

// CHALLENGE(PHASE-2): Add a "Delete" button next to each document that alerts the document ID when clicked.
