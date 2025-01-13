# Problem: https://leetcode.com/problems/maximum-gap
# Runtime: 777 ms

class Solution:
    # [9, 6, 10,12,15]
    # 

    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        best = 0
        for i in range(len(nums) - 1):
            best = max(best, abs(nums[i] - nums[i + 1]))
        return best