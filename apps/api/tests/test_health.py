from unittest.mock import patch


def test_health_endpoint_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_ready_endpoint_returns_503_when_db_unavailable(client):
    with patch("app.api.routes.health._check_db_connectivity", return_value=False):
        response = client.get("/ready")
    assert response.status_code == 503
    data = response.json()
    assert data["status"] == "unhealthy"


def test_ready_endpoint_returns_200_when_db_available(client):
    with patch("app.api.routes.health._check_db_connectivity", return_value=True):
        response = client.get("/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
