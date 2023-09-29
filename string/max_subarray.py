from types import List
class Solution:
    def max_subarray(self, arr: List[int]) -> int:
        res = arr[0]
        maxEnding = arr[0]
        # iterate through the array
        # remember the sum of the previous contigous array before the current element
        # add the prev sum to the current element
        # now you have two choices
        # either accept the new sum (prev sum + arr[i])
        # or discard it and start fresh with arr[i]
        # it depends if the new sum is greater than the arr[i], if it is greater, we make the new sum as the new prev sum, else we consider the arr[i] as the new prev sum and move ahead
        for i in arr:
            maxEnding = max(maxEnding+arr[i], arr[i])
            res = max(res, maxEnding)
        return res