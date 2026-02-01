# # Naive
# we loop through each element
# for each element , we find the max bar to its left, and max bar to it right
# the difference between these two is the amount of water that will get trapped, 
# BUT reduce the amount with the element at the current index
# because it is a bar of that height there, so no water gets trapped

def trap_water(arr):
  result = 0
  for i in range(1, len(arr) - 1): # we loop through the entire loop
    # we need to the left max bar
    left_max = arr[i] # we start with the current element as the max 
    # and loop through from the first element to the element prevous to the curreent element
    for j in range(0, i):
      left_max = max(left_max, arr[j])
    # we need to the rght max bar
    right_max = arr[j] # we assign the current element (the current element is j same as i actually) as right max
    # and then loop from j to end of array and find the max on the right side
    for j in range(i+1, n):
      right_max = max(right_max, arr[j])

    #now the result is 
    result = result + (right_max - left_max) - arr[i]

    
  
    
