from types import List
class Solution:
    def check_two_sum(self, nums: List[int], target: int) -> List[int]:
        prevMap={} # val : index
        # iterate through the list along with its index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:#if the diff is in map, it means we have a two sum
                return [prevMap[diff], i]
            prevMap[n] = i #if the number is not in the map, add it to the map