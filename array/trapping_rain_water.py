# # Naive
# we loop through each element
# for each element , we find the max bar to its left, and max bar to it right
# the minimum between these two is the amount of water that will get trapped, 
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

#Efficient
def trap_water(arr):
  result = 0
  # create a new array that has the left_max for each element , and create another array that has right_max for each element
  # now when you iterate, you aleady know the left max for the preevious element, so when you know it, compare that to the current element
  # and if the current element is greater then update the left max for the element, other the previous elements's left max is also the 
# current the currrent elements left max
  l_max = [0] * len(arr)
  r_max = [0] * len(arr)

  for i in range(1, n): # go from element 1 to last element
    if arr[i] > l_max[i-1]:
      l_max[i] = arr[i]
    else:
      l_max[i] = l_max[i-1]
  r_max[n-1] = arr[n-1]
  for i in range(n-1, -1, -1): #go reverse from second last element to first element
    r_max[i] = max(r_max[i+1] , arr[])

  #
  for i in range(1, n-1):
    result = result + min(l_max[i], r_max[]) - arr[i]
  return result
    


  

    
  
    

