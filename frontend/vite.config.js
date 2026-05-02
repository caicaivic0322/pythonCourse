import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
  optimizeDeps: {
    exclude: ['pyodide']
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (!id.includes('node_modules')) return

          // Markdown rendering (~500KB)
          if (id.includes('react-markdown') || id.includes('remark-gfm') ||
              id.includes('mdast') || id.includes('unified') || id.includes('micromark') ||
              id.includes('hast') || id.includes('unist')) {
            return 'markdown'
          }

          // Code editor - Monaco (~2MB, lazy loaded)
          if (id.includes('@monaco-editor') || id.includes('monaco-editor')) {
            return 'editor'
          }

          // Syntax highlighting for markdown code blocks (~200KB)
          if (id.includes('react-syntax-highlighter') || id.includes('prismjs') ||
              id.includes('refractor')) {
            return 'syntax-highlighter'
          }

          // Animations (~130KB)
          if (id.includes('framer-motion')) {
            return 'animation'
          }

          // Routing
          if (id.includes('react-router-dom') || id.includes('react-router')) {
            return 'router'
          }

          // React core
          if (id.includes('react-dom') || id.includes('/react/') ||
              id.includes('scheduler')) {
            return 'react-vendor'
          }

          // Icons (~200KB)
          if (id.includes('lucide-react')) {
            return 'icons'
          }

          // Network
          if (id.includes('axios')) {
            return 'network'
          }
        },
      },
    },
  },
})
