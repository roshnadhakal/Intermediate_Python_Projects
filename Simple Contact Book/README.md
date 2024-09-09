# Contact Book Program

A simple command-line application for managing a contact book. This program allows users to add, remove, search, and display contacts, as well as save and load contacts from a file.

## Features

- **Add Contact**: Add new contacts with name, phone number, and email.
- **Remove Contact**: Remove existing contacts by name.
- **Search Contact**: Search for a contact by name and display their details.
- **Display All Contacts**: View all contacts stored in the contact book.
- **Save and Load Contacts**: Automatically save contacts to a file and load them at startup.

## How to Use

1. **Run the Program**: Execute the `contact_book.py` script in your terminal.
2. **Menu Options**: You will see a menu with the following options:
   - **1. Add Contact**: Input the contact's name, phone number, and email.
   - **2. Remove Contact**: Enter the name of the contact you wish to remove.
   - **3. Search Contact**: Input the name of the contact you want to find.
   - **4. Display All Contacts**: View all saved contacts.
   - **5. Exit**: Save all contacts to a file and exit the program.
3. **Follow Prompts**: Follow the on-screen prompts to interact with the contact book.

## Code Structure

The program is structured into several functions:

- `display_menu()`: Displays the main menu options.
- `add_contact()`: Prompts the user to add a new contact.
- `remove_contact()`: Removes a contact from the list by name.
- `search_contact()`: Searches for a contact by name and displays their details.
- `display_all_contacts()`: Displays all contacts in the contact book.
- `save_contacts()`: Saves the current contacts to a file.
- `load_contacts()`: Loads contacts from a file at startup.

## Requirements

- Python 3.12.4 or higher

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
