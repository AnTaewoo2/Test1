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
