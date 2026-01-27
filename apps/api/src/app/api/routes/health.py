import socket
from datetime import datetime, timezone

from fastapi import APIRouter, Response, status

from app.config import settings
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
        sock = socket.create_connection(
            (settings.db_host, settings.db_port), timeout=2
        )
        sock.close()
        return True
    except OSError:
        return False
