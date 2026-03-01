def search_in_infinite_array(arr, target):
    """
    Search for a target element in an infinite-sized array.
    
    Approach:
    1. Find the range where target might exist using exponential jumps
    2. Apply binary search on that range
    
    Time Complexity: O(log n) where n is the position of target
    Space Complexity: O(1)
    """
    
    # Step 1: Find the range using exponential search
    if arr[0] == target:
        return 0
    
    # Find range [left, right] where target exists
    left = 0
    right = 1
    
    while arr[right] < target:
        left = right
        right *= 2
    
    # Step 2: Binary search in the found range
    return binary_search(arr, target, left, right)


def binary_search(arr, target, left, right):
    """Binary search in the given range."""
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Element not found


# Example usage
if __name__ == "__main__":
    # Simulating infinite array with a large list
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    
    target = 10
    result = search_in_infinite_array(arr, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")