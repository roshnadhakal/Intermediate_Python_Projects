# Task Scheduler

This Python script allows you to schedule daily tasks and receive reminders at specified times. The tasks are read from a text file, and reminders are printed to the console when the tasks are due.

## Requirements

- Python 3.12.4
- `schedule` library (You can install it using `pip install schedule`)
- .txt file to store tasks
- `time` library (included in Python standard library)

## Code Explanation

1. **Imports**:
   The script imports the necessary libraries: 
   - `schedule` for scheduling tasks.
   - `time` for handling time-related operations.

2. **Reading Tasks**:
   The `read_tasks` function reads tasks from a file named "tasks.txt". Each task should be in the format "HH:MM Task Description" (e.g., "09:00 Water the plants"). The function returns a list of tasks.

3. **Sending Reminders**:
   The `send_reminder` function is responsible for printing a reminder message when a scheduled task is due. It takes the task description as an argument.

4. **Scheduling Tasks**:
   The `schedule_tasks` function is used to schedule tasks from the file. It calls the `read_tasks` function to get the list of tasks, then splits each task into the time (HH:MM) and the task description. It schedules each task to run every day at the specified time using the `schedule.every().day.at()` method. The `send_reminder` function is called with the task description as an argument when the scheduled time arrives.

5. **Main Execution Block**:
   In the `if __name__ == "__main__":` block, the `schedule_tasks` function is called with the filename "tasks.txt" to set up the task schedules.

6. **Infinite Loop**:
   An infinite loop is used to continuously check for pending tasks using `schedule.run_pending()`. This ensures that the tasks are run when their scheduled time arrives.

7. **CPU Management**:
   Inside the loop, `time.sleep(1)` is used to pause execution for 1 second to avoid consuming too much CPU resources.

## Usage

1. Create a file named "tasks.txt" in the same directory as the Python script.
2. Add tasks to the "tasks.txt" file, one task per line, in the format "HH:MM Task Description" (e.g., "09:00 Water the plants").
3. Run the Python script.
4. The script will read the tasks from the file, schedule them to run every day at the specified times, and continuously check for pending tasks.
5. When a scheduled task is due, a reminder message will be printed to the console.

## Example Output

Assuming your `tasks.txt` contains:
09:00 Water the plants  
10:30 Attend team meeting  
15:00 Take a break 
  
When you run your script and it reaches each scheduled time, you would see output similar to:  
Reminder: Water the plants  
Reminder: Attend team meeting  
Reminder: Take a break  

## Contributing
Contributions are welcome! If you would like to contribute to this project,fork this repository or pull request.
