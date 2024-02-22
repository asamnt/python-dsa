def smallest_difference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne, idxTwo = 0, 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        #we pick two numbers one from each array
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        #we always calculate the current difference
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1#if firstNum is smaller we shift the idxOne one place to the right so that when we shift we are definitely going to get a biggger number than the current and hence the difference is going to reduce
        elif firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1#if secondNum is greater we shift the idxtwo one place to the right so that when we shify we are definitely going to get a biggger number than the current and hence the difference is going to reduce
        else:
            return [firstNum, secondNum] #if they are same then we have our answer
        if smallest > current:# if the current smallest is smaller than the prev smallest, we replace and add the current pair to the smallest pair array
            smallest = current
            smallestPair= [firstNum, secondNum]
    return smallestPair


print(smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))