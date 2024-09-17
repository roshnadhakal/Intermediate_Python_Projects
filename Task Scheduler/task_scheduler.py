import schedule # schedule task to run at specific time or intervals
import time # time module to get current time

""" 
Function to read task from a file
Each task should be in the format "HH:MM Task Description"
"""
def read_task(filename):
    with open(filename, 'r') as f:
        # reading the file line by line, stripping extra spaces, removing empty lines
        return [line.strip() for line in f if line.strip()]
    

"""
Function to handle sending reminders
This action will be triggered when a scheduled task is due
"""
def send_reminder(task):
    print(f"Reminder: {task}")



# Function to schedule tasks from file
def schedule_tasks(filename):
    tasks = read_task("tasks.txt") # you can change the filename accorsing to yours
    for task in tasks:
        # split the task into time(HH:MM) and description
        time_str, task_description = task.split(' ', 1) # only the first space is used for splitting
        
        """
        schedule task to run everyday at specified time
        The send_reminder function is called with task_description as args
        """
        schedule.every().day.at(time_str).do(send_reminder, task_description)

# Call the function to set up task schedules
if __name__ == "__main__":
    schedule_tasks("tasks.txt")

    # Infinite loop to  continuously check for pending task
    # This insure that the task are run when their scheduled time arrives
    while True:
        schedule.run_pending()
        time.sleep(1)  # wait for 1 sec to avoid consuming too much CPU




        


