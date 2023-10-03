def selection_sort(data : list):
    n = len(data)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            # check with every other element in the list and if it is greater, then update min_ind to the index of that element
            # this way we get the min of the current list
            if data[j] < data[min_index]:
                #swap
                min_index = j
        # once we get the min_index of the list, we swap
        data[min_index], data[i] = data[i], data[min_index]
        #so in the first loop we get the min of the current list
l = [10, 5, 8, 20, 2, 18]

selection_sort(l)

print(*l)