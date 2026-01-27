from uuid import uuid4


def test_create_item(client):
    response = client.post("/items", json={"name": "Test Item", "description": "A test"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "A test"
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_list_items(client):
    client.post("/items", json={"name": "Item 1"})
    client.post("/items", json={"name": "Item 2"})

    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 2
    assert len(data["items"]) == 2


def test_get_item_by_id(client):
    create_resp = client.post("/items", json={"name": "Fetch Me"})
    item_id = create_resp.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Fetch Me"


def test_get_item_not_found(client):
    response = client.get(f"/items/{uuid4()}")
    assert response.status_code == 404


def test_update_item(client):
    create_resp = client.post("/items", json={"name": "Original"})
    item_id = create_resp.json()["id"]

    response = client.put(f"/items/{item_id}", json={"name": "Updated"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"


def test_update_item_not_found(client):
    response = client.put(f"/items/{uuid4()}", json={"name": "Nope"})
    assert response.status_code == 404


def test_delete_item(client):
    create_resp = client.post("/items", json={"name": "Delete Me"})
    item_id = create_resp.json()["id"]

    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404


def test_delete_item_not_found(client):
    response = client.delete(f"/items/{uuid4()}")
    assert response.status_code == 404
