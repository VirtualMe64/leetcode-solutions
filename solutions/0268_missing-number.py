# Problem: https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalTrue = 0
        total = 0
        n = len(nums)
        for i in range(n):
            totalTrue += i
            total += nums[i]
        return n + totalTrue - total