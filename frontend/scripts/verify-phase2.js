const fs = require('fs');
const path = require('path');

const projectRoot = path.resolve(__dirname, '..');

console.log('\n🧠 DevBrain — Phase 2 Verification');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');

let passedCount = 0;
const totalTests = 8;

function runTest(name, fn) {
  try {
    fn();
    console.log(`  \x1b[32m✓\x1b[0m ${name}`);
    passedCount++;
  } catch (error) {
    console.log(`  \x1b[31m✗\x1b[0m ${name}`);
    console.log(`     \x1b[33mReason:\x1b[0m ${error.message}`);
  }
}

// Test 1: Next.js 15+ App Router setup
runTest('Next.js initialized with App Router', () => {
  const layoutPath = path.join(projectRoot, 'app/layout.tsx');
  const pagePath = path.join(projectRoot, 'app/page.tsx');
  if (!fs.existsSync(layoutPath)) throw new Error('Missing app/layout.tsx');
  if (!fs.existsSync(pagePath)) throw new Error('Missing app/page.tsx');
});

// Test 2: Tailwind CSS v4 configured
runTest('Tailwind CSS v4 configured', () => {
  const globalsCssPath = path.join(projectRoot, 'app/globals.css');
  if (!fs.existsSync(globalsCssPath)) throw new Error('Missing app/globals.css');
  const content = fs.readFileSync(globalsCssPath, 'utf8');
  if (!content.includes('@import "tailwindcss"') && !content.includes('@theme') && !content.includes('tailwind')) {
    throw new Error('Tailwind CSS import or theme configuration not found in app/globals.css');
  }
});

// Test 3: shadcn/ui configured
runTest('shadcn/ui installed and configured', () => {
  const configPath = path.join(projectRoot, 'components.json');
  if (!fs.existsSync(configPath)) throw new Error('Missing components.json');
  const content = JSON.parse(fs.readFileSync(configPath, 'utf8'));
  if (!content.style || !content.tailwind) {
    throw new Error('shadcn/ui configuration in components.json is incomplete');
  }
});

// Test 4: TS Strict Mode
runTest('TypeScript strict mode enabled', () => {
  const tsconfigPath = path.join(projectRoot, 'tsconfig.json');
  if (!fs.existsSync(tsconfigPath)) throw new Error('Missing tsconfig.json');
  const content = fs.readFileSync(tsconfigPath, 'utf8');
  if (!content.includes('"strict": true')) {
    throw new Error('"strict": true not found in tsconfig.json');
  }
});

// Test 5: Main Sidebar layout
runTest('Root layout with sidebar navigation implemented', () => {
  const layoutPath = path.join(projectRoot, 'app/layout.tsx');
  const content = fs.readFileSync(layoutPath, 'utf8');
  if (!content.includes('<SidebarProvider') || !content.includes('<AppSidebar')) {
    throw new Error('SidebarProvider and AppSidebar wrappers are not rendered in app/layout.tsx');
  }
  
  const sidebarPath = path.join(projectRoot, 'components/layout/app-sidebar.tsx');
  if (!fs.existsSync(sidebarPath)) throw new Error('Missing components/layout/app-sidebar.tsx');
  const sidebarContent = fs.readFileSync(sidebarPath, 'utf8');
  if (!sidebarContent.includes('navItems.map') || !sidebarContent.includes('pathname === item.url')) {
    throw new Error('Navigation menu with active route checking is not implemented correctly in app-sidebar.tsx');
  }
});

// Test 6: Dashboard page
runTest('Dashboard page with mock metrics implemented', () => {
  const pagePath = path.join(projectRoot, 'app/page.tsx');
  const content = fs.readFileSync(pagePath, 'utf8');
  if (!content.includes('stats.map') || !content.includes('Card') || !content.includes('<CardHeader')) {
    throw new Error('Metrics grid mapping over stats not found or not rendering Cards in app/page.tsx');
  }
});

// Test 7: Documents list page
runTest('Documents list page implemented', () => {
  const docsPagePath = path.join(projectRoot, 'app/documents/page.tsx');
  if (!fs.existsSync(docsPagePath)) throw new Error('Missing app/documents/page.tsx');
  const content = fs.readFileSync(docsPagePath, 'utf8');
  if (!content.includes('mockDocuments.map') || !content.includes('statusColors[')) {
    throw new Error('mockDocuments list or colored status badges not found or not rendered in app/documents/page.tsx');
  }
});

// Test 8: Dark mode toggle
runTest('Dark mode toggle working', () => {
  const togglePath = path.join(projectRoot, 'components/theme-toggle.tsx');
  if (!fs.existsSync(togglePath)) throw new Error('Missing components/theme-toggle.tsx');
  const content = fs.readFileSync(togglePath, 'utf8');
  if (!content.includes('useTheme') || !content.includes('setTheme(') || !content.includes('onClick={')) {
    throw new Error('Theme toggle does not use next-themes to control theme state or onClick trigger is missing');
  }
  
  // Make sure they filled in the toggle logic
  if (content.includes('// TODO(PHASE-2): Implement toggle logic.') && !content.includes('setTheme(theme ===')) {
    throw new Error('Theme toggle click handler logic is missing or empty');
  }
});

console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
if (passedCount === totalTests) {
  console.log(`\x1b[32m✅ Success! ${passedCount}/${totalTests} tests passing.\x1b[0m`);
  process.exit(0);
} else {
  console.log(`\x1b[31m❌ Failed! Only ${passedCount}/${totalTests} tests passing.\x1b[0m`);
  process.exit(1);
}
