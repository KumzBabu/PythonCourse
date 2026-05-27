# ============================================================
# PROJECT 2: Todo List App
# Concepts used: lists, dicts, loops, file I/O, JSON
# ============================================================

import json
import os

SAVE_FILE = "todos.json"

def load_todos():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE) as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(SAVE_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def show_todos(todos):
    print("\n[LIST] Your Todo List:")
    if not todos:
        print("  (empty — add something!)")
        return
    for i, todo in enumerate(todos, 1):
        status = "[DONE]" if todo["done"] else "[ ]"
        print(f"  {i}. {status} {todo['task']}")

def add_todo(todos):
    task = input("Enter task: ").strip()
    if task:
        todos.append({"task": task, "done": False})
        save_todos(todos)
        print(f"[DONE] Added: '{task}'")

def complete_todo(todos):
    show_todos(todos)
    try:
        num = int(input("Mark which # as done? ")) - 1
        if 0 <= num < len(todos):
            todos[num]["done"] = True
            save_todos(todos)
            print(f"[DONE] Marked as done: '{todos[num]['task']}'")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def delete_todo(todos):
    show_todos(todos)
    try:
        num = int(input("Delete which #? ")) - 1
        if 0 <= num < len(todos):
            removed = todos.pop(num)
            save_todos(todos)
            print(f"[DEL] Deleted: '{removed['task']}'")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def main():
    todos = load_todos()
    print("=" * 35)
    print("   [TODO] Todo List App")
    print("=" * 35)

    while True:
        print("\n1. Show todos")
        print("2. Add todo")
        print("3. Mark as done")
        print("4. Delete todo")
        print("5. Quit")

        choice = input("\nChoose: ").strip()

        if choice == "1": show_todos(todos)
        elif choice == "2": add_todo(todos)
        elif choice == "3": complete_todo(todos)
        elif choice == "4": delete_todo(todos)
        elif choice == "5":
            print("Goodbye! ")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
