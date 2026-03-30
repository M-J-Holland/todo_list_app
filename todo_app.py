todos = []
print("Welcome to the CLI TODO app!")

user_choice = input("Would you like to 'add', 'show', 'edit', 'complete' or 'exit'? ").strip().lower()
if user_choice == 'add':
    todo_to_add = input("Enter your todo to add it to the todos list: ")
    todos.append(todo_to_add)
elif user_choice == "show":
    for todo_index, todo in enumerate(todos, start=1):
        print(f"{todo_index}. {todo}")
