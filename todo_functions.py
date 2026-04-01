from input_output import write_todos


def add_todo(todos):
    """Add a new todo to the list."""
    todo = input("Enter a todo: ").strip()

    if not todo:
        print("Todo cannot be empty.")
        return

    todos.append(todo)
    write_todos(todos)
    print(f"Added: {todo}")


def show_todos(todos):
    """Show all todos in the list."""
    if not todos:
        print("No todos to show.")
        return

    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo}")


def get_valid_todo_index(todos, prompt):
    """Ask the user for a valid todo number and return its index."""
    while True:
        user_input = input(prompt).strip()

        if not user_input.isdigit():
            print("Please enter a number.")
            continue

        todo_index = int(user_input) - 1

        if 0 <= todo_index < len(todos):
            return todo_index

        print("That todo number does not exist.")


def edit_todo(todos):
    """Edit an existing todo."""
    if not todos:
        print("No todos to edit.")
        return

    show_todos(todos)
    todo_index = get_valid_todo_index(
        todos,
        "Enter the number of the todo you want to edit: "
    )

    new_todo = input("Enter the new todo: ").strip()

    if not new_todo:
        print("Todo cannot be empty.")
        return

    old_todo = todos[todo_index]
    todos[todo_index] = new_todo
    write_todos(todos)

    print(f"Changed '{old_todo}' to '{new_todo}'.")


def complete_todo(todos):
    """Remove a todo from the list."""
    if not todos:
        print("No todos to complete.")
        return

    show_todos(todos)
    todo_index = get_valid_todo_index(
        todos,
        "Enter the number of the todo you want to complete: "
    )

    removed_todo = todos.pop(todo_index)
    write_todos(todos)

    print(f"Completed: {removed_todo}")