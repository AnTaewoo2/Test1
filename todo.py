class TodoStore:
    def __init__(self):
        self._todos = []
        self._next_id = 1

    def add(self, text):
        todo = {
            "id": self._next_id,
            "text": text,
            "completed": False,
        }
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def list(self):
        return self._todos.copy()

    def complete(self, todo_id):
        for todo in self._todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                return todo
        raise KeyError(todo_id)

    def delete(self, todo_id):
        for index, todo in enumerate(self._todos):
            if todo["id"] == todo_id:
                del self._todos[index]
                return todo
        raise KeyError(todo_id)

