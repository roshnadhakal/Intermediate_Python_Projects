#Function to load existing expenses from a file
def load_expenses():
    try:
        with open("expenses.txt", "r") as f:
            #Read all lines in the file, strip newline char and convert into floats
            expenses = [float(line.strip()) for line in f.readlines()]
            return expenses
    except FileNotFoundError:
        #If the file doesnot exist, return an empty list
        return[]


#Function to save expenses to a file
def save_expenses(expenses):
    #open expenses.txt file in write mode
    with open("expenses.txt", "w") as f:
        #Write each expense on a new line in the file
        for expense in expenses:
            f.write(str(expense)+ "\n")


#Function to add a new expense
def add_expense(expenses):
    while True:
        try:
            #Ask user for the expense amount
            expense = float(input("Enter the expense amount: Rs."))
            #Add the expense to the list
            expenses.append(expense)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


#Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        #If there are no expenses, print a message
        print("No expenses recorded.")
    else:
        #Print all expenses
        print("Expenses:")
        #Enumerate the expenses and print them with their index
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense}")

#Main Function
def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__  == "__main__":
    main()


