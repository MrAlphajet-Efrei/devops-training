import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client():
    application = create_app()
    with TestClient(application) as c:
        yield c
