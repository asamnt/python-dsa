def remove_duplicate(arr):
    res = 1
    for i in range(1, len(arr)):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res += 1
    return res