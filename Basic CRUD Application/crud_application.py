# Create a file to store the tasks
task_file = 'task.txt'

# Function to load tasks from the file
def load_tasks():
    tasks = []  # Create an empty list
    try:
        with open(task_file, 'r') as f:
            # Read all the lines from the file and store them in a list
            tasks = f.readlines()
            # Remove newline characters from each line
            tasks = [task.strip() for task in tasks]
    except FileNotFoundError:
        print(f"The file {task_file} does not exist.")
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(task_file, 'w') as f:
        for task in tasks:
            # Write each task to a new line in the file
            f.write(task + '\n')

# Function to display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour tasks are:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print("\n")

# Function to create a new task
def create_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()  # Load existing tasks
    tasks.append(task)    # Add the new task to the list
    save_tasks(tasks)     # Save the updated list of tasks to the file
    print("Task added successfully.\n")

# Function to update a task
def update_task():
    tasks = load_tasks()
    display_tasks(tasks)  # Display all tasks
    if not tasks:
        return
    
    try:
        # Get the index of the task to update
        task_id = int(input("Enter the task number you want to update: ")) - 1
        if 0 <= task_id < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_id] = new_task
            save_tasks(tasks)
            print("Task updated successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

# Function to delete a task
def delete_task():
    tasks = load_tasks()
    display_tasks(tasks)  # Display all tasks
    if not tasks:
        return
    
    try:
        # Get the index of the task to delete
        task_id = int(input("Enter the task number you want to delete: ")) - 1
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)  # Remove the task at the given number
            save_tasks(tasks)
            print("Task deleted successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

# Main Program Loop
def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_task()  # Call the function to create a new task
        elif choice == '2':
            tasks = load_tasks()  # Load and display tasks
            display_tasks(tasks)  # Display all tasks
        elif choice == '3':
            update_task()  # Call the function to update a task
        elif choice == '4':
            delete_task()  # Call the function to delete a task
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

if __name__ == "__main__":
    main()
