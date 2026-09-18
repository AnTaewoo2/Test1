import pytest

from todo import TodoStore


def test_add_returns_todo_with_id_text_and_completed_state():
    store = TodoStore()

    assert store.add("buy milk") == {
        "id": 1,
        "text": "buy milk",
        "completed": False,
    }


def test_list_returns_todos_in_creation_order():
    store = TodoStore()

    store.add("one")
    store.add("two")

    assert store.list() == [
        {"id": 1, "text": "one", "completed": False},
        {"id": 2, "text": "two", "completed": False},
    ]


def test_complete_marks_existing_todo_completed():
    store = TodoStore()
    store.add("task")

    assert store.complete(1) == {
        "id": 1,
        "text": "task",
        "completed": True,
    }
    assert store.list() == [
        {"id": 1, "text": "task", "completed": True},
    ]


def test_delete_removes_existing_todo():
    store = TodoStore()
    store.add("task")

    assert store.delete(1) == {
        "id": 1,
        "text": "task",
        "completed": False,
    }
    assert store.list() == []


def test_complete_and_delete_unknown_ids_raise_key_error():
    store = TodoStore()

    with pytest.raises(KeyError):
        store.complete(99)

    with pytest.raises(KeyError):
        store.delete(99)

