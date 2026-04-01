from todo_functions import *

todos = []
print("Welcome to the CLI TODO app!")


def main():
    try:
        while True:
            user_choice = input("Would you like to 'add', 'show', 'edit', 'complete' or 'exit'? ").strip().lower()
            if user_choice == "add":
                add_todo()

            elif user_choice == "show":
                if not check_todos(todos):
                    show_todos(todos)

            elif user_choice == "edit":
                if not check_todos(todos):
                    edit_todos()
            elif user_choice == 'complete':
                if check_todos(todos):
                    complete_todos()

            elif user_choice == 'exit':
                print("Thank you for using the TODO app, goodbye!")
                break
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected, closing down the TODO app.")


main()
