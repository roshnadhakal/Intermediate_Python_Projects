# Binary Search Implementation in Python

## Overview

This repository contains a simple implementation of the binary search algorithm in Python. Binary search is an efficient algorithm for finding an item from a sorted list of items.  
It works by repeatedly dividing the search interval in half, making it much faster than linear search for large datasets.

## Features

- Efficient search algorithm with O(log n) time complexity.
- Easy to understand and implement.
- User-friendly input and output.

## Requirements

- Python 3.12.4 or higher

## Usage

You can run the binary search script directly from the terminal. The script prompts the user to input a target number to search for in a predefined sorted list.

## Code Explanation

The binary search algorithm is implemented in the \`binary_search\` function. Below is a brief overview of how the code works:

### Function Definition

\`\`\`python
def binary_search(sorted_list, target):
\`\`\`

- **Parameters**:
  - \`sorted_list\`: A sorted list of elements.
  - \`target\`: The element to search for.

### Initializing Indices

\`\`\`python
low = 0
high = len(sorted_list) - 1
\`\`\`

- **\`low\`**: Starting index of the search (0).
- **\`high\`**: Ending index of the search (last index).

### Main Loop

\`\`\`python
while low <= high:
\`\`\`

- Continues searching while there are elements between \`low\` and \`high\`.

### Finding the Midpoint

\`\`\`python
mid = (low + high) // 2
\`\`\`

- Calculates the midpoint index.

### Checking the Midpoint Value

\`\`\`python
if sorted_list[mid] == target:
    return mid
\`\`\`

- Returns \`mid\` if the target is found.

### Adjusting the Search Range

\`\`\`python
elif sorted_list[mid] < target:
    low = mid + 1
\`\`\`

- Updates \`low\` to search the upper half.

\`\`\`python
else:
    high = mid - 1
\`\`\`

- Updates \`high\` to search the lower half.

### Target Not Found

\`\`\`python
return -1
\`\`\`

- Returns \`-1\` if the target is not found in the list.


### Sample Output

\`\`\`
Enter an element from 1-10: 5
Element 5 found at index 4
\`\`\`

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

