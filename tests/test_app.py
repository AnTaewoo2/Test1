import app as app_module
from todo import TodoStore


def test_get_todos_starts_empty():
    app_module.store = TodoStore()
    client = app_module.app.test_client()

    response = client.get("/todos")

    assert response.status_code == 200
    assert response.get_json() == {"todos": []}


def test_post_todos_creates_and_lists_todo():
    app_module.store = TodoStore()
    client = app_module.app.test_client()

    response = client.post("/todos", json={"text": "read"})

    assert response.status_code == 201
    assert response.get_json() == {
        "id": 1,
        "text": "read",
        "completed": False,
    }

    response = client.get("/todos")

    assert response.status_code == 200
    assert response.get_json() == {
        "todos": [
            {
                "id": 1,
                "text": "read",
                "completed": False,
            }
        ]
    }


def test_complete_todo():
    app_module.store = TodoStore()
    client = app_module.app.test_client()
    client.post("/todos", json={"text": "read"})

    response = client.post("/todos/1/complete")

    assert response.status_code == 200
    assert response.get_json() == {
        "id": 1,
        "text": "read",
        "completed": True,
    }


def test_delete_todo():
    app_module.store = TodoStore()
    client = app_module.app.test_client()
    client.post("/todos", json={"text": "read"})

    response = client.delete("/todos/1")

    assert response.status_code == 200
    assert response.get_json() == {
        "id": 1,
        "text": "read",
        "completed": False,
    }

    response = client.get("/todos")

    assert response.get_json() == {"todos": []}


def test_invalid_requests_return_json_errors():
    app_module.store = TodoStore()
    client = app_module.app.test_client()

    response = client.post("/todos", data="{", content_type="application/json")

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "text must be a non-empty string",
    }

    response = client.post("/todos", json={"text": ""})

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "text must be a non-empty string",
    }

    response = client.post("/todos/not-an-id/complete")

    assert response.status_code == 400
    assert response.get_json() == {"error": "invalid todo id"}

    response = client.delete("/todos/99")

    assert response.status_code == 404
    assert response.get_json() == {"error": "todo not found"}
