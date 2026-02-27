# todo.py

import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['title']}")

def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        tasks[index]["completed"] = True
        print("Task updated.")
    except:
        print("Invalid selection.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        print("Task deleted.")
    except:
        print("Invalid selection.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1.Add  2.View  3.Complete  4.Delete  5.Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
