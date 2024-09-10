def binary_search(sorted_list, target):
     """
    Perform a binary search on a sorted list to find the target element.
    Parameters:
    sorted_list (list): A list of elements sorted in ascending order.
    target: The element to search for in the sorted list.
    Returns:
    int: The index of the target element if found, otherwise -1.
    """
     low = 0 # initialize the low index to 0
     high = len(sorted_list) -1 #initialize the high index to last element

    #continue to search until low pointer is less than or equal to high
     while low <= high: 
            mid = (low + high) // 2 # calculate the mid index

        # Check if the target is present at mid
            if sorted_list[mid] == target:  
                return mid  # Target found, return the index
        
        #check if the mid element is less than the target
            elif sorted_list[mid] < target:
                low = mid + 1  # Update the low index to mid + 1
        
        # If the mid element is greater than the target
            else:
                high = mid - 1  # Update the high index to mid - 1

     return -1 #target was not found  in the list


# Example Use

if __name__ == "__main__":
   sorted_list = [1,2,3,4,5,6,7,8,9,10]
   target = int(input("enter element from 1-10: "))
   result = binary_search(sorted_list, target)

   if result != -1:
        print(f"Element {target} found at index {result}")

   else:
       print(f"Element {target} not found in the list.")


