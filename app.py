from flask import Flask, jsonify, request

from todo import TodoStore


app = Flask(__name__)
store = TodoStore()


def _error(message, status):
    return jsonify({"error": message}), status


def _parse_todo_id(todo_id):
    try:
        return int(todo_id)
    except ValueError:
        return None


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify({"todos": store.list()}), 200


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get("text"), str) or not data["text"]:
        return _error("text must be a non-empty string", 400)

    return jsonify(store.add(data["text"])), 201


@app.route("/todos/<todo_id>/complete", methods=["POST"])
def complete_todo(todo_id):
    parsed_id = _parse_todo_id(todo_id)
    if parsed_id is None:
        return _error("invalid todo id", 400)

    try:
        todo = store.complete(parsed_id)
    except KeyError:
        return _error("todo not found", 404)

    return jsonify(todo), 200


@app.route("/todos/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    parsed_id = _parse_todo_id(todo_id)
    if parsed_id is None:
        return _error("invalid todo id", 400)

    try:
        todo = store.delete(parsed_id)
    except KeyError:
        return _error("todo not found", 404)

    return jsonify(todo), 200
