def check_todos(_todos):
    """Function that checks if there are any todos in the list"""
    if len(todos) > 0:
        return True
    return False


def add_todo():
    """Function that adds a todo to to todos list."""
    todo_to_add = input("Enter your todo to add it to the todos list: ")
    todos.append(todo_to_add)
    print(f"Your todo: '{todo_to_add}' has been added to the list.")


def show_todos(_todos):
    """Function that shows all todos in the list"""

    for todo_index, todo in enumerate(todos, start=1):
        print(f"{todo_index}. {todo}")


def edit_todos():
    """Function that edits the user-selected todo in the list."""
    todo_to_edit = input("Enter the number for the todo you would like to edit: ")
    while True:
        try:
            todo_to_edit = int(todo_to_edit) - 1
            if todo_to_edit < 0 or todo_to_edit >= len(todos):
                print("Invalid todo number. Please try again.")
                todo_to_edit = input("Enter the number for the todo you would like to edit: ")
                continue
            new_todo = input("Enter your new todo: ")
            todos[todo_to_edit] = new_todo
            print(f"Your old todo has been edited to {new_todo}")
            break
        except ValueError:
            print("Invalid input, please only enter a number")
            todo_to_edit = input("Enter the number for the todo you would like to edit: ")
            continue


def complete_todos():
    """A function that completes the user-selected todo."""
    todo_to_complete = input("Enter the number for the todo you would like to complete: ")
    while True:
        try:
            todo_to_complete = int(todo_to_complete) - 1
            if todo_to_complete < 0 or todo_to_complete >= len(todos):
                print("Invalid todo number. Please try again.")
                todo_to_complete = input("Enter the number for the todo you would like to complete: ")
                continue
            todos.pop(todo_to_complete)
            print("Your todo has been completed and removed from the list.")
            break
        except ValueError:
            print("Invalid input, please only enter a number")
            todo_to_complete = input("Enter the number for the todo you would like to complete: ")
            continue