def reverse_list(arr):
    start = 0
    end = len(l) -1
    while start < end:
        arr[start], arr[end] = arr[end], start[start]
        start += 1
        end -= 1
