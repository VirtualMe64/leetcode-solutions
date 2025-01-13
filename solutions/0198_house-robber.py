# Problem: https://leetcode.com/problems/house-robber
# Runtime: 0 ms

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for house in nums:
            best = max(house + prev2, prev1)
            prev2 = prev1
            prev1 = best
        return prev1