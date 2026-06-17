# FoodAI

AI-powered food recommendation and restaurant management platform.

## Sprint 1

FoodAI Sprint 1 delivers a FastAPI backend with PostgreSQL, SQLAlchemy, Alembic, JWT authentication, restaurant and menu domains, AI recommendation skeleton, Docker support, and CI workflow.

## Run locally

1. Copy `backend/.env.example` to `backend/.env`.
2. Start the stack:

```bash
docker-compose up --build
```

3. Open API docs:

- `http://localhost:8000/api/v1/docs`

## Project structure

- `backend/` - FastAPI backend source
- `docker-compose.yml` - local development services
- `.github/workflows/ci.yml` - CI pipeline
- `docs/sprint1.md` - Sprint 1 summary
