/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#3b82f6", // Blue for main actions
        secondary: "#10b981", // Green for success
        accent: "#f59e0b", // Orange for fun elements
        dark: "#1e293b", // Slate for background
        light: "#f8fafc", // Slate for text
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Fredoka', 'sans-serif'], // Fun font for headers
      },
    },
  },
  plugins: [],
}
