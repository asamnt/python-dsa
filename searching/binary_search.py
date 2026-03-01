def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1
        else:
            return mid

# Test cases
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 7
    print(binarySearch(arr, x))  # Output: 6 (index of element 7)
    
    x = 10
    print(binarySearch(arr, x))  # Output: -1 (element not found)   


