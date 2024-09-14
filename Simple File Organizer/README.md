# File Organizer

## Overview
`file_organizer.py` is a Python script designed to help users organize files within a specified directory by sorting them into subdirectories based on their file extensions. This tool is particularly useful for maintaining a tidy file structure and quickly locating files.

## Requirements
- Python 3.12.4 or higher

## How It Works
The script performs the following steps:

1. **Directory Input**: Prompts the user to enter the path of the directory they wish to organize.
2. **File Type Identification**: 
   - It scans the specified directory and identifies the file extensions of all files present.
   - A dictionary is created to group files by their respective extensions.
3. **Directory Creation**: 
   - For each unique file extension, a new subdirectory is created (if it doesn’t already exist) within the original directory.
4. **File Movement**: 
   - The script moves each file into its corresponding subdirectory based on its extension.
5. **Completion Message**: Once all files have been organized, a success message is displayed.

## Usage
To use the script, follow these steps:

1. Ensure you have Python 3.12.4 installed on your machine.
2. Download or clone the repository containing `file_organizr.py`.
3. Open a terminal and navigate to the directory where the script is located.
4. Run the script using the command:
   ```bash
   python file_organizr.py
   ```
5. When prompted, enter the path of the directory you wish to organize.

## Example
If you have the following files in a directory:

```
- document.txt
- image.png
- script.py
- notes.docx
```

After running the script, the directory structure will be organized as follows:

```
- document.txt
- image.png
- script.py
- notes.docx
- txt/
    - document.txt
- png/
    - image.png
- py/
    - script.py
- docx/
    - notes.docx
```

## Important Notes
- Make sure you have the necessary permissions to create directories and move files within the specified directory.
- The script does not handle duplicate filenames. If two files have the same name but different extensions, they will be moved to their respective directories without conflict.
