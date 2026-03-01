def first_occurrence(arr, target):
    """
    Find the first occurrence of a target number in a sorted array.
    
    Args:
        arr: A sorted list of integers
        target: The number to search for
    
    Returns:
        The index of the first occurrence, or -1 if not found
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5, 5, 6]
    target = 2
    
    index = first_occurrence(arr, target)
    print(f"First occurrence of {target}: {index}")  # Output: 1