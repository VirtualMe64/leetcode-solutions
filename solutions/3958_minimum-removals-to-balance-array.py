# Problem: https://leetcode.com/problems/minimum-removals-to-balance-array
# Runtime: 71 ms

from bisect import bisect_right

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        # right = 1
        # best = len(nums) - 1

        # for left in range(len(nums) - 1):
        #     while right < len(nums) and nums[right] <= nums[left] * k:
        #         right += 1
        #     cost = left + len(nums) - right
        #     best = min(best, cost)
        
        # return best

        i = 0
        for num in nums:
            if num > nums[i] * k:
                i += 1
        return i