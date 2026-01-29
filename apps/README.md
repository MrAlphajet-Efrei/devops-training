# DevOps Demo — Local Stack

Docker Compose configuration to run the full stack locally (PostgreSQL, API, Frontend).

## Quick Start

```bash
cd apps

# Create your environment file from the template
cp .env.example .env

# Start all services (builds images on first run)
docker compose up --build

# Or start in detached mode
docker compose up -d --build
```

## Services

| Service    | URL                    | Image / Build        |
|------------|------------------------|----------------------|
| PostgreSQL | `localhost:5432`       | `postgres:15-alpine` |
| API        | `http://localhost:8000`| Built from `./api`   |
| Frontend   | `http://localhost:3000`| Built from `./frontend` |

## Environment Variables

All variables are defined in `.env.example` with sensible defaults. The compose file also provides inline defaults, so the stack works even without a `.env` file.

| Variable               | Default        | Description                  |
|------------------------|----------------|------------------------------|
| `DB_NAME`              | `devops_demo`  | PostgreSQL database name     |
| `DB_USER`              | `app_user`     | PostgreSQL user              |
| `DB_PASSWORD`          | `changeme`     | PostgreSQL password          |
| `DEBUG`                | `false`        | API debug mode               |
| `NEXT_PUBLIC_API_URL`  | `http://localhost:8000` | API URL for frontend |

## Health Checks

Each service has a health check configured:

| Service    | Method                          | Interval |
|------------|---------------------------------|----------|
| PostgreSQL | `pg_isready`                    | 10s      |
| API        | Python urllib → `/health`       | 30s      |
| Frontend   | `wget` → `http://localhost:3000`| 30s      |

Services start in dependency order: PostgreSQL → API → Frontend. Each waits for the previous service to be healthy before starting.

## Common Commands

```bash
# View logs
docker compose logs -f

# Check service health status
docker compose ps

# Rebuild a specific service
docker compose build api

# Stop services
docker compose down

# Stop and remove volumes (resets database)
docker compose down -v
```
