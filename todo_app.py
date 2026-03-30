todos = []
print("Welcome to the CLI TODO app!")

user_choice = input("Would you like to 'add', 'show', 'edit', 'complete' or 'exit'? ").strip().lower()
if user_choice == 'add':
    todo_to_add = input("Enter your todo to add it to the todos list: ")
    todos.append(todo_to_add)
elif user_choice == "show":
    for todo_index, todo in enumerate(todos, start=1):
        print(f"{todo_index}. {todo}")
elif user_choice == "edit":
    todo_to_edit = input("Enter the number for the todo you would like to edit: ")
    try:
        todo_to_edit = int(todo_to_edit) - 1
        if todo_to_edit < 0 or todo_to_edit >= len(todos):
            print("Invalid todo number. Please try again.")
        else:
            new_todo = input("Enter your new todo to ")
            todos[todo_to_edit] = new_todo
    except ValueError:
        print("Invalid input, please only enter a number")