def stock_buy_and_sell(arr):
  profit = 0
  for i in range(1, len(arr)):
    if arr[i] > arr[i-1]: # if the current element is greater than previous element, means there is a profit
      profit = profit + (arr[i] - arr[i-1]) #if theree is a profit, then we add to the existing profit, we accumulate
    # if there is a dip, we ignore that , as there is no profit
    # we again add the diff, when we see the value rising, that is current element is greater than previus element
      return profit
    
