# Task Plan: Python Learning Platform (Gamified)

## Goal
Build a Python learning website for students (GESP level 4) with a playful/gamified UI, online code runner, and teacher admin panel.
Stack: React (Vite) + Django (DRF).

## Phases

### Phase 1: Project Initialization
- [x] Create project structure (frontend/backend directories)
- [x] Initialize React project (Vite)
- [x] Initialize Django project
- [x] Setup basic configuration (CORS, DRF)

### Phase 2: Frontend Core (Gamified UI)
- [x] Install dependencies (Tailwind, Framer Motion, Axios)
- [x] Create Gamified Layout (Navbar, Sidebar, Background)
- [x] Implement Routing (Home, Course List, Course Detail, Login/Register)

### Phase 3: Backend Core & Auth
- [x] Create `users` app (Custom User Model)
- [x] Create `courses` app (Models for Course, Chapter, Lesson)
- [x] Implement Auth API (Login, Register, Token)
- [x] Setup Django Admin for Teacher approval

### Phase 4: Course Content & Features
- [x] Implement Course Listing & Detail API
- [x] Frontend: Course Player UI
- [x] Implement Quizzes (Backend models + Frontend UI) - *Implemented as Lesson Type*
- [x] Implement "Code Runner" (Mock/Sandboxed execution) - *Implemented Mock Runner*

### Phase 5: Polish & Finalize
- [x] UI Polish (Animations, Themes)
- [x] Seed initial data (Head First Python chapters)
- [x] Final Review
- [x] Create test user for Admin demonstration
