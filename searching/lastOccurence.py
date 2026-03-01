def last_occurrence(arr, target):
    """
    Find the last occurrence of target in a sorted array.
    
    Args:
        arr: Sorted list of integers
        target: Element to find
        
    Returns:
        Index of last occurrence, or -1 if not found
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid  # Store this position
            left = mid + 1  # Continue searching in right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# Test cases
if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    print(last_occurrence(arr, 2))  # Output: 3
    print(last_occurrence(arr, 5))  # Output: 8
    print(last_occurrence(arr, 1))  # Output: 0
    print(last_occurrence(arr, 7))  # Output: -1