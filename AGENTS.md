# Repository Guidelines

## Project Structure & Module Organization
The repo is split into `backend/` and `frontend/`. `backend/` contains the Django 5 API, with project settings in `backend/config/` and app code in `backend/users/` and `backend/courses/`; data/bootstrap scripts such as `seed_gesp_courses.py` and `create_superuser.py` live alongside `manage.py`. `frontend/` is a Vite + React client: page-level routes are in `frontend/src/pages/`, shared UI lives in `frontend/src/components/`, layouts in `frontend/src/layouts/`, API setup in `frontend/src/api/`, and app-wide styles in `frontend/src/styles/`.

## Build, Test, and Development Commands
Backend setup:
```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python seed_gesp_courses.py
python manage.py runserver
```
Use `python manage.py test` to run Django tests and `./build.sh` to install deps, collect static files, migrate, and seed data for deployment.

Frontend setup:
```bash
cd frontend
npm install
npm run dev
```
Use `npm run build` for a production bundle, `npm run preview` to inspect it locally, and `npm run lint` before opening a PR.

## Coding Style & Naming Conventions
Follow existing conventions in each stack. Python uses 4-space indentation, `snake_case` for functions/modules, and Django app naming patterns. React files use PascalCase for components and pages (`CourseDetail.jsx`), camelCase for hooks/context values, and colocated `*.module.css` files for page/component styling. Keep imports explicit and avoid unused variables; frontend linting is enforced by `frontend/eslint.config.js`.

## Testing Guidelines
Backend tests belong in each app’s `tests.py` or a local `tests/` package and should cover serializers, permissions, and API behavior for changed endpoints. Run `python manage.py test` from `backend/` before submitting. There is no frontend test runner configured yet, so frontend changes must at minimum pass `npm run lint` and include brief manual verification steps in the PR.

## Commit & Pull Request Guidelines
Recent history uses short, imperative Conventional Commit-style subjects such as `feat: safe update content logic` and `chore: Add render.yaml blueprint`. Prefer `feat:`, `fix:`, `chore:`, or `docs:` prefixes and keep each commit focused. PRs should include a concise summary, affected areas (`backend`, `frontend`, or both), setup/migration notes, linked issues, and screenshots or short recordings for UI changes.

## Security & Configuration Tips
Keep secrets in environment variables, especially `SECRET_KEY` and database settings. `backend/config/settings.py` allows all hosts and all CORS origins for development; tighten those values before production deployment.
