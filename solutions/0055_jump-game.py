# Problem: https://leetcode.com/problems/jump-game
# Runtime: 12 ms

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastReachable = len(nums) - 1
        curr = lastReachable
        while curr > 0:
            curr -= 1
            if curr + nums[curr] >= lastReachable:
                lastReachable = curr
        return nums[0] >= lastReachable