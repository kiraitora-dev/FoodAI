# FoodAI Backend

This directory contains the FastAPI backend for FoodAI.

## Setup

1. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

2. Build and run with Docker Compose from the repository root:

```bash
docker-compose up --build
```
```

3. API docs:

- `http://localhost:8000/api/v1/docs`

## Notes

- Uses PostgreSQL via Docker Compose.
- Migrations are run automatically when the backend container starts.
- OpenAI integration requires `OPENAI_API_KEY` to be set in the environment.
