def move_element_to_end(array, toMove):
    i = 0
    j = len(array)-1
    while i < j:
        while i < j and array[j] == toMove: 
            #check if the current item at idx-to-move(j) is same as the toMove item
            # if we do find it is same, we move the idx one to the left
            # and we do it till only i is less than j
            j -= 1
        if array[i] == toMove:
            #if current element is the same as toMove element, we swap with element at j idx
            array[i], array[j] = array[j] , array[i]
        i += 1
    return array

print(move_element_to_end([4,2,7,3,1,6,2,2], 2))

