# Problem: https://leetcode.com/problems/maximum-total-subarray-value-i
# Runtime: 12 ms

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k