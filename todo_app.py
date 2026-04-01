from input_output import read_todos
from todo_functions import add_todo, show_todos, edit_todo, complete_todo

todo_options = {"add": add_todo,
                "show": show_todos,
                "edit": edit_todo,
                "complete": complete_todo
                }


def main():
    print("Welcome to the CLI TODO app!")
    todos = []
    try:
        while True:
            user_choice = input("Would you like to 'add', 'show', 'edit', 'complete' or 'exit'? ").strip().lower()
            if user_choice == "exit":
                print("Thank you for using the TODO app, goodbye!")
                break
            user_action = todo_options.get(user_choice)
            if user_action is None:
                print("Invalid choice. Please try again.")
                continue
            user_action(todos)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected, closing down the TODO app.")


if __name__ == "__main__":
    main()
