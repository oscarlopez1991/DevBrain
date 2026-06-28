// ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Sidebar Layout with Next.js App Router & shadcn/ui
//
// In React, we compose components. Instead of ASP.NET layout helpers, we use
// components from our UI library (shadcn/ui Sidebar in this case) and map over
// lists of links to construct navigation.
//
// Key Concepts:
// - "use client" is required because we use usePathname() hook to determine active route.
// - usePathname() from 'next/navigation' is the React Router/Next.js equivalent to
//   checking the current URL pathname (e.g. checking ActionContext.ActionDescriptor in ASP.NET).
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"use client"

import { usePathname } from "next/navigation"
import Link from "next/link"
import { Home, FileText, Search, MessageSquare, Settings, Brain } from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarFooter,
  SidebarHeader,
} from "@/components/ui/sidebar"
import { ThemeToggle } from "@/components/theme-toggle"

const navItems = [
  { title: "Dashboard", url: "/", icon: Home },
  { title: "Documents", url: "/documents", icon: FileText },
  { title: "Search", url: "/search", icon: Search },
  { title: "Chat", url: "/chat", icon: MessageSquare },
  { title: "Settings", url: "/settings", icon: Settings },
]

export function AppSidebar() {
  const pathname = usePathname()

  return (
    <Sidebar collapsible="icon">
      {/* Sidebar Header */}
      <SidebarHeader className="border-b border-border p-4 flex flex-row items-center gap-2">
        <Brain className="h-6 w-6 text-primary animate-pulse" />
        <span className="font-semibold text-lg tracking-tight group-data-[collapsible=icon]:hidden">
          DevBrain
        </span>
      </SidebarHeader>

      {/* Sidebar Navigation */}
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel className="group-data-[collapsible=icon]:hidden">Navigation</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {/* TODO(PHASE-2): Build the sidebar navigation links.
                  Requirements:
                  1. Map over the `navItems` array.
                  2. Use the Next.js <Link> component instead of raw <a> tags to prevent full page reloads.
                  3. Use `pathname === item.url` to determine if a route is currently active.
                  4. Apply active styling (e.g., bg-accent or text-primary) to the SidebarMenuButton if active.
                  
                  Pista: Use the `isActive` attribute or add conditional classes using `cn()` utility.
              */}
              {navItems.map((item) => {
                const isActive = pathname === item.url
                return (
                  <SidebarMenuItem key={item.title}>
                    <SidebarMenuButton
                      isActive={isActive}
                      tooltip={item.title}
                      render={
                        <Link href={item.url}>
                          <item.icon className="h-4 w-4" />
                          <span>{item.title}</span>
                        </Link>
                      }
                    />
                  </SidebarMenuItem>
                )
              })}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>

      {/* Sidebar Footer with Theme Toggle */}
      <SidebarFooter className="border-t border-border p-4 flex flex-row items-center justify-between group-data-[collapsible=icon]:justify-center">
        <div className="flex items-center gap-2 group-data-[collapsible=icon]:hidden">
          <div className="h-8 w-8 rounded-full bg-primary/10 flex items-center justify-center font-bold text-xs text-primary">
            JD
          </div>
          <div className="flex flex-col">
            <span className="text-xs font-semibold">Jane Doe</span>
            <span className="text-[10px] text-muted-foreground">User</span>
          </div>
        </div>
        <ThemeToggle />
      </SidebarFooter>
    </Sidebar>
  )
}

// CHECK(PHASE-2): Run `pnpm dev` and check if:
// 1. Sidebar is collapsible (by clicking trigger in layout).
// 2. Active item is highlighted based on current path.
// 3. Navigation transitions are smooth and client-side (no browser spinners).

// CHALLENGE(PHASE-2): Add a badge to "Documents" item showing mock total document count.
