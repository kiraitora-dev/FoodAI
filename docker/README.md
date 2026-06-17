# Docker support for FoodAI

This repository uses Docker Compose for local development.

## Run locally

1. Copy the backend environment example:

```bash
cp backend/.env.example backend/.env
```

2. Start services:

```bash
docker-compose up --build
```

3. Visit the API docs:

- `http://localhost:8000/api/v1/docs`

## Notes

- The API service depends on PostgreSQL.
- Database migrations are applied automatically when the backend container starts.
