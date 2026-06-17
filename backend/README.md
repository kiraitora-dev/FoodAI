# FoodAI Backend

This directory contains the FastAPI backend for the FoodAI project.

## Requirements

- Python 3.12+
- PostgreSQL (local or via Docker Compose)
- Docker and Docker Compose for local containerized development

## Setup

1. Copy the example environment file:

```bash
cp backend/.env.example backend/.env
```

2. Start the stack from the repository root:

```bash
docker-compose up --build
```

3. The API will be available at:

- `http://localhost:8000/api/v1/docs`

## Notes

- The backend container runs `alembic upgrade head` before starting.
- If you want to run tests locally, install the dependencies and execute:

```bash
pip install -r backend/requirements.txt
pytest -q
```
