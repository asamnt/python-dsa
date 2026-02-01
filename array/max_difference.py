# if we get to subtract from the current element the minimum of the elements to the left, we get the max diff so far with the current element
def max_diff(arr):
  result = arr[1]-arr[0]
  min_val = arr[0]
  for i in range(1, len(arr)):
    # you are at the current element
    # you need to calculate the current diff i.e diff between the current element and 
    # the min_val(you already have a min_val you are tracking) so far
    # so if the current diff is geater than the previous result, update the result
    result = max(result , arr[i] - min_val) 
    min_val = min(min_val , arr[i])
  retuen result
    
