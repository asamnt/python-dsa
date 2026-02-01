def remove_duplicate(arr):
    res = 1
    for i in range(1, len(arr)):
        if arr[res-1] != arr[i]: #if the current element is not the same as previous element indicated by res index
            arr[res] = arr[i] # then copy over the element from i to where res is 
            res += 1
    return res

# if the element at res index and i is same, we skip it, that is move ahead
