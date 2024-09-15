# Directory Tree Printer

## Overview
The Directory Tree Printer is a Python script that visualizes the structure of directories and files in a specified path. It prints a tree-like format to the console, making it easier to understand the hierarchy of files and folders.

## Requirements
- Python 3.12.4 or later
- Operating System: Compatible with Windows, macOS, and Linux

## Installation
1. Ensure you have Python 3.12.4 installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
2. Clone this repository or download the script file.


## Usage
To use the Directory Tree Printer, simply run the script with the desired path as an argument. The script will print the directory structure starting from the specified path.

### Example
To print the directory structure of `F:\path`, execute the following command in your terminal: You

```bash
python directory_tree.py
```

### Code Explanation
The core function of the script is `print_tree(path, level=0)`, which performs the following:
- **Arguments**:
  - `path`: The path to the directory or file that you want to visualize.
  - `level`: The current level of indentation, defaulting to zero for the root level.
  
- **Functionality**:
  - It iterates over the contents of the specified directory.
  - For each item, it constructs the full path and checks if it's a directory or a file.
  - Directories are printed with a trailing slash (`/`) and indented according to their depth in the hierarchy.
  - Files are printed without a trailing slash and also indented.

## Example Output
When you run the script, you might see output like this:

```
|-- Folder1/
  |-- Subfolder1/
  |-- Subfolder2/
|-- File1.txt
|-- File2.txt
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
