todos = []
print("Welcome to the CLI TODO app!")
try:
    while True:
        user_choice = input("Would you like to 'add', 'show', 'edit', 'complete' or 'exit'? ").strip().lower()
        if user_choice == 'add':
            todo_to_add = input("Enter your todo to add it to the todos list: ")
            todos.append(todo_to_add)
            print(f"Your todo: '{todo_to_add}' has been added to the list.")

        elif user_choice == "show":
            if not todos:
                print("You have no todos to show, please add some todos first then come back and see them.")
            else:
                for todo_index, todo in enumerate(todos, start=1):
                    print(f"{todo_index}. {todo}")

        elif user_choice == "edit":
            if not todos:
                print("You have no todos to edit, please add some todos first then come back and edit them.")
            else:
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

        elif user_choice == 'complete':
            if not todos:
                print("You have no todos to complete, please add some todos first then come back and complete them.")
            else:
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

        elif user_choice == 'exit':
            print("Thank you for using the TODO app, goodbye!")
            break
except KeyboardInterrupt:
    print("\nKeyboard interrupt detected, closing down the TODO app.")
