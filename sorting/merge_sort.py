def merge_subarray(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high + 1]
    i, j , k = 0,0, low
    while i < len(left) and  j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k +=1
            i +=1
        else:
            arr[k] = right[j]
            k +=1
            j +=1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

def merge_sort(arr, l, r):
    if r > l:
        mid = (l + r) // 2
        merge_sort(arr, l, mid) # merge sort left sub array
        merge_sort(arr, mid+1, r) #merge sort right sub array
        merge_subarray(arr, l, mid, r) #merge the sorted arrays
    return arr

l = [10, 15, 20, 40, 8, 11, 55]
print(merge_sort(l, 0, 6))
