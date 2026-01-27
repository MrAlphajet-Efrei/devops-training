from datetime import datetime, timezone

from fastapi import APIRouter, Response, status
from sqlalchemy import text

from app.db.session import engine
from app.models.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="healthy", timestamp=datetime.now(timezone.utc))


@router.get("/ready", response_model=HealthResponse)
async def ready(response: Response) -> HealthResponse:
    if _check_db_connectivity():
        return HealthResponse(status="healthy", timestamp=datetime.now(timezone.utc))

    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return HealthResponse(status="unhealthy", timestamp=datetime.now(timezone.utc))


def _check_db_connectivity() -> bool:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
