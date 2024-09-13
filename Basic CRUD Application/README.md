# Python Task Manager

This is a simple command-line task manager written in Python 3.12.4. It allows users to create, read, update, and delete tasks stored in a text file.

## Features

- Create new tasks
- Read all existing tasks
- Update existing tasks
- Delete tasks
- Persistent storage using a text file

## Requirements

- Python 3.12.4 or higher

## Installation

1. Clone the repository or download the code files.
2. Ensure you have Python 3.12.4 installed on your machine.
3. Navigate to the project directory in your terminal.

## Usage

Run the task manager by executing the following command in your terminal:

python task_manager.py

Follow the on-screen instructions to manage your tasks.

## Code Explanation

### Task File

- The tasks are stored in a file named `task.txt`. This file is created in the same directory as the script if it doesn't already exist.

### Functions

1. **load_tasks()**: 
   - Loads tasks from `task.txt` into a list. It handles the case where the file might not exist by catching a `FileNotFoundError`.

2. **save_tasks(tasks)**: 
   - Saves the current list of tasks back to `task.txt`, with each task on a new line.

3. **display_tasks(tasks)**: 
   - Displays all tasks to the user. If there are no tasks, it informs the user accordingly.

4. **create_task()**: 
   - Prompts the user to enter a new task, loads existing tasks, adds the new task to the list, and saves the updated list.

5. **update_task()**: 
   - Allows the user to update an existing task. It displays the current tasks, prompts for the task number to update, and saves the changes.

6. **delete_task()**: 
   - Enables the user to delete a task by specifying its number. It updates the task list accordingly.

### Main Program Loop

- The `main()` function provides a menu-driven interface for the user to interact with the task manager. It continues to prompt the user until they choose to exit.

## Contributing

Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.
