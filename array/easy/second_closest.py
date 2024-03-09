def second_closest(arr, x):
    closest = int("-inf")
    for i in arr:
        if i < x and (closest == -1 or x-closest > x-i):
            closest= i
    return closest