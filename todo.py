# todo.py - Simple Console-based To-Do List Application

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the text file into a list."""
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass  # If file doesn't exist, start with an empty to-do list
    return tasks


def save_tasks(tasks):
    """Save the list of tasks into the text file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available!\n")
        return

    print("\n------ YOUR TO-DO LIST ------")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("------------------------------\n")


def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!\n")
    else:
        print("Task cannot be empty!\n")


def remove_task(tasks):
    """Remove a task by number."""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("===========================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)

        elif choice == "4":
            save_tasks(tasks)
            print("\nGoodbye! Your tasks are saved.\n")
            break

        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
