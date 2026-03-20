import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    exclude: ['pyodide']
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (!id.includes('node_modules')) return

          if (id.includes('react-markdown') || id.includes('remark-gfm')) {
            return 'markdown'
          }

          if (id.includes('@monaco-editor') || id.includes('monaco-editor')) {
            return 'editor'
          }

          if (id.includes('react-router-dom')) {
            return 'router'
          }

          if (id.includes('react-dom') || id.includes('/react/')) {
            return 'react-vendor'
          }

          if (id.includes('lucide-react')) {
            return 'icons'
          }

          if (id.includes('axios')) {
            return 'network'
          }
        },
      },
    },
  },
})
