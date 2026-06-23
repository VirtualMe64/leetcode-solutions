# Problem: https://leetcode.com/problems/count-elements-with-at-least-k-greater-values
# Runtime: 89 ms

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        # 1, 2, 3
        
        if k >= len(nums):
            return 0

        if k == 0:
            return len(nums)

        ref = len(nums) - k       # 2
        idx = len(nums) - k - 1   # 1
        while idx >= 0 and nums[idx] >= nums[ref]:
            idx -= 1

        return idx + 1