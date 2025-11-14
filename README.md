📝 To-Do List Application (Console-Based)

This is a simple command-line To-Do List application built using Python.
It allows you to add, view, and remove tasks, with tasks stored permanently in a text file.

📌 Features

✔ View Tasks

Displays all the tasks saved in the to-do list.

✔ Add Task

Allows the user to add a new task to the list.

✔ Remove Task

Removes a task based on the task number.

✔ Persistent Storage

All tasks are stored in tasks.txt, so your to-do list remains saved even after exiting the program.

📂 File Structure
todo.py
tasks.txt   (automatically created after running the program)

▶️ How to Run the Program

Make sure Python is installed on your system.

Open the terminal or VS Code terminal.

Navigate to the folder where todo.py is saved.

Run the script:

python todo.py

🧠 How It Works

The app runs in a loop and displays a menu with the following options:

1. View Tasks
2. Add Task
3. Remove Task
4. Exit


Selecting Option 1 shows all tasks.

Selecting Option 2 asks you to enter a new task.

Selecting Option 3 asks for the task number to delete.

Selecting Option 4 saves all tasks and exits the program.

📁 Data Storage

The program uses a text file named tasks.txt to store tasks:

When the program starts, it loads tasks from this file.

When tasks are added or removed, the file updates automatically.

✔ Requirements 

1. Use of lists for task management

2. Implementation of add / remove / view functionality

3. Use of open() for file handling

4. Persistent CLI to-do app
