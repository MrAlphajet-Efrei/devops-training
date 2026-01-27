# DevOps Learning API

FastAPI backend service for the DevOps Learning Platform. Provides health check and readiness endpoints for Kubernetes liveness and readiness probes.

## Prerequisites

- Python 3.11+
- pip

## Installation

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -e ".[dev]"
```

## Running Locally

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

## Running Tests

```bash
pytest -v
pytest -v --cov=app --cov-report=term-missing
```

## Endpoints

| Method | Path      | Purpose         | Response                                    |
| ------ | --------- | --------------- | ------------------------------------------- |
| `GET`  | `/health` | Liveness probe  | `{"status": "healthy", "timestamp": "..."}` |
| `GET`  | `/ready`  | Readiness probe | 200 OK or 503 Service Unavailable           |

## Docker

```bash
# Build
docker build -t devops-api:0.1.0 .

# Run
docker run -d -p 8000:8000 devops-api:0.1.0

# Verify
curl http://localhost:8000/health
```

The image uses multi-stage builds with `python:3.11-slim` and runs as non-root user `appuser` (UID 1000).

## Environment Variables

| Variable      | Default     | Description       |
| ------------- | ----------- | ----------------- |
| `DB_HOST`     | localhost   | Database hostname |
| `DB_PORT`     | 5432        | Database port     |
| `DB_NAME`     | devops_demo | Database name     |
| `DB_USER`     | app_user    | Database username |
| `DB_PASSWORD` | (empty)     | Database password |
| `DEBUG`       | false       | Enable debug mode |
