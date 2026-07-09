// ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Root Layout component (RSC)
//
// In ASP.NET MVC, this is your `_Layout.cshtml`. It wraps all pages and defines
// global HTML structures, global CSS loads, and the layout wrapper structure.
//
// In Next.js, we also wrap the page with context providers (like ThemeProvider and
// SidebarProvider) at the layout level so all subpages share the same theme state
// and layout configuration.
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import type { Metadata } from "next";
import { geistMono, geistSans } from "@/lib/fonts";
import "./globals.css";

import { ThemeProvider } from "@/components/theme-provider"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/layout/app-sidebar"

export const metadata: Metadata = {
  title: "DevBrain — Document Intelligence",
  description: "AI-Powered Document Intelligence Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
      suppressHydrationWarning
    >
      <body className="min-h-full bg-background font-sans text-foreground">
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
          <SidebarProvider>
            <AppSidebar/>
            <main className="flex-1 flex flex-col h-screen overflow-y-auto">
              <SidebarTrigger/>
              {children}
            </main>
          </SidebarProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}

// CHECK(PHASE-2): Run `pnpm dev`.
// ✅ Open http://localhost:3000 and verify the side menu collapses and expands correctly.
// ✅ Verify that dark mode updates the header and main background color correctly.

