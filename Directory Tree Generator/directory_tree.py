import os

def print_tree(path, level = 0):
    """
    Prints a visual tree structure of directories and files.

    Args:
        path(str): The path to directory or file
        level(int, optional): The indentation level, default to zero.
    """
    # Iterate over the content of directory at the given path
    for item in os.listdir(path):
        # Construct the full path to the item
        item_path = os.path.join(path, item)

        # Check is the item is a directory
        if os.path.isdir(item_path):
            # Print the directory name with indentation
            print('  ' * level + '|--' + item + '/' )
            # Recursively print the tree structure of the subdirectory
            print_tree(item_path, level + 1)
        else:
            # Print the file name with indentation
            print('  ' * level + '|--' + item)

print_tree('F:\path')
     
