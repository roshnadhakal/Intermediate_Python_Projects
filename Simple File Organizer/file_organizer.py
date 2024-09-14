# file_organizr.py
import os

# Function to organize files in a given directory
def organize_files(directory):
    # Create a dictionary to store files by their extension (type)
    file_types = {}

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Split the filename and extension using os.path.splitext
        # This returns a tuple (root, ext), where ext is the file extension
        file_ext = os.path.splitext(filename)[1][1:]  # Extract the extension without the dot

        # If the extension (file type) is not already in the dictionary, add it
        if file_ext not in file_types:
            file_types[file_ext] = []  # Initialize an empty list for this file type

        # Append the file to the list of files for its extension/type
        file_types[file_ext].append(filename)

    # Create directories and move files based on their type
    for file_type, files in file_types.items():
        # Create a new directory path for each file type using os.path.join
        # os.path.join combines multiple path components into a single path
        file_type_dir = os.path.join(directory, file_type)

        # Check if the directory for this file type already exists
        if not os.path.exists(file_type_dir):
            # If the directory does not exist, create it using os.makedirs
            # os.makedirs can create directories recursively if needed
            os.makedirs(file_type_dir)

        # Move each file to its corresponding directory
        for file in files:
            # Create the source path of the file (original location)
            src = os.path.join(directory, file)
            # Create the destination path (new location in the type-based directory)
            dst = os.path.join(file_type_dir, file)

            # Use os.rename to move the file from source to destination
            # os.rename can be used to move or rename files
            os.rename(src, dst)

    # Inform the user that the organization process is complete
    print("Files organized successfully!!")

# Main Function
def main():
    # Get the directory path to organize from the user
    directory = input("Enter the directory to organize: ")

    # Call the organize_files function to organize the files in the specified directory
    organize_files(directory)

# Entry point of the script
if __name__ == "__main__":
    main()
