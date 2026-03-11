# Project: CLI To-Do List Manager
# Author: Tharun
# Description: A command line task management application that allows users
#              to add, view, and delete daily tasks using a menu-driven interface.
# Concepts Used: loops, functions, lists, conditional statements, user input

TASK_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()