# Expense Tracker

A simple command-line application written in Python to track personal expenses. This program allows users to add, view, and save expenses to a file.

## Requirements

- Python 3.12.4 or higher


## Usage

1. Run the program:
   ```bash
   python expense_tracker.py
   ```

2. Follow the on-screen menu to add or view expenses.

## Code Explanation

### Functions

- **load_expenses()**: 
  - This function attempts to read existing expenses from a file named `expenses.txt`. It returns a list of expenses as floats. If the file does not exist, it returns an empty list.

- **save_expenses(expenses)**: 
  - This function takes a list of expenses and writes each expense to `expenses.txt`, with each expense on a new line.

- **add_expense(expenses)**: 
  - This function prompts the user to enter a new expense amount. It validates the input to ensure it is a number and appends the valid expense to the list.

- **view_expenses(expenses)**: 
  - This function displays all recorded expenses. If there are no expenses, it informs the user accordingly. It enumerates the expenses for better readability.

### Main Functionality

- **main()**: 
  - This is the entry point of the program. It loads existing expenses, displays a menu for user interaction, and handles user choices for adding expenses, viewing expenses, or exiting the program.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add!
