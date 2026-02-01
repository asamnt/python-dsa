def isSorted(arr):
  i = 1
  while i < len(arr):
    if arr[i] < arr[i-1]:
      return False
    i = i + 1
  return True
