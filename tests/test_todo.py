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
