def read_todos(filename="todos.txt"):
    """Read todos from a file and return them as a list."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def write_todos(todos, filename="todos.txt"):
    """Write todos to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        for todo in todos:
            file.write(todo + "\n")