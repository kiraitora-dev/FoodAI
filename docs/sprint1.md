# FoodAI Sprint 1

## Completed in Sprint 1

- Backend FastAPI scaffold with versioned API routing.
- PostgreSQL support via SQLAlchemy AsyncIO and Alembic migrations.
- JWT authentication with access and refresh token support.
- Restaurant and menu item domains.
- Category and order domains added.
- AI recommendation skeleton with OpenAI integration fallback.
- Docker environment with root `docker-compose.yml` and backend `Dockerfile`.
- CI workflow with lint and tests in `.github/workflows/ci.yml`.

## Backend structure

- `backend/app/main.py`
- `backend/app/api/router.py`
- `backend/app/api/routes`
- `backend/app/core`
- `backend/app/db`
- `backend/app/models`
- `backend/app/schemas`
- `backend/app/services`
- `backend/app/repositories`
- `backend/tests`

## How to run

1. Copy `.env.example` to `backend/.env`.
2. Start the stack:

```bash
docker-compose up --build
```

3. API docs available at:

- `http://localhost:8000/api/v1/docs`

## Notes

- OpenAI calls require `OPENAI_API_KEY` in environment.
- Database migrations are configured with Alembic.
