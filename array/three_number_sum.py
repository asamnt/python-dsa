def three_number_sum(array, target_sum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):#the last number in the loop should have aleast two other values to assign pointer to, so we iterate only till len -2
        left = i + 1
        right = len(array) - 1
        while left < right:#while pointers are not overlapping or passing each other
            currentSum = array[i]+array[left]+array[right]
            if currentSum == target_sum:
                triplets.append([array[i],array[left],array[right]])
                #increment left and decrement right - as we move on
                left += 1
                right -=1
            elif currentSum < target_sum:#if the current sum is less then we must move only the left pointer to the right as that will help us increase the sum
                left += 1
            elif currentSum > target_sum:#f the current sum is greater then we must move only the right pointer to the left as that will help us decrease the sum
                right -=1
    return triplets


print(three_number_sum([12,3,1,2,-6,5,-8,6],0))


