# Contact Book Program

# Initialize an empty list to store contacts
contacts = []

# Display the contact book menu
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Exit")

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    # Append a dictionary containing the contact details to the contacts list
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

# Function to remove a contact by name
def remove_contact():
    name = input("Enter name of contact to remove: ")
    # Loop through the contacts list to find the contact by name
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)  # Remove the contact if found
            print("Contact removed successfully!")
            return
    print("Contact not found!")

# Function to search for a contact by name
def search_contact():
    name = input("Enter name of contact to search: ")
    for contact in contacts:
        if contact["name"] == name:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return
    print("Contact not found!")

# Function to display all contacts in the contacts list
def display_all_contacts():
    for contact in contacts:  # Loop through each contact in the list
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print()  # Print an empty line for readability

# Function to save contacts to a text file
def save_contacts():
    # Open file in write mode and write each contact's details 
    with open("contacts.txt", "w") as f:
        for contact in contacts:
            f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

# Function to load contacts from the text file at program startup
def load_contacts():
    global contacts  # modify the contacts list defined at the top, rather than creating a new local variable.
    try:
        # Open the contacts file and read each line
        with open("contacts.txt", "r") as f:
            contacts = []  # Reset contacts list before loading
            for line in f:
                # Strip whitespace and split each line by commas into name, phone, and email
                name, phone, email = line.strip().split(",")
                # Append each contact as a dictionary to the contacts list
                contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        print("File Not Found ")
        

# Load contacts from file when the program starts
load_contacts()

# Main program loop
while True:
    display_menu()  # Show the menu
    choice = input("Enter your choice: ")
    
    # Handle the user input based on the menu choice
    if choice == "1":
        add_contact()
    elif choice == "2":
        remove_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        display_all_contacts()
    elif choice == "5":
        save_contacts()  # Save contacts before exiting the program
        break
    else:
        print("Invalid choice. Please try again.")
