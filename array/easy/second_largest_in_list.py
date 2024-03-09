# two iterations
def get_second_largest_naive(l):
    if len(l) <= 1:
        return None
    largest = get_largest(l)
    second_largest = None
    for i in l:
        if i != largest:
            if second_largest == None:
                second_largest = i
            else:
                second_largest = max(second_largest, i)
    return second_largest


def get_largest(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1, len(l)):
            if l[i] > res:
                res = l[i]
        return res
    
# one iteration
def second_largest_optimal(l):
    if len(l) <= 1 :
        return None
    largest = l[0]
    second_largest = None
    for x in l:
        if x > largest:
            second_largest = largest
            largest = x
        elif x != largest:
            if second_largest == None or x > second_largest:
                second_largest = x
    return second_largest