from types import List
class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        l, r =0, len(numbers) -1
        # left pointer and right pointer approach
        # shift either of the pointers depending on the sum they make
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l, r]
        return []

    
