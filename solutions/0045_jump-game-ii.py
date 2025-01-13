# Problem: https://leetcode.com/problems/jump-game-ii
# Runtime: 2700 ms

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[len(nums) - 1] = 0
        for i in range(len(nums) - 2, -1, -1):
            currMin = len(nums) + 1
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
              currMin = min(currMin, 1 + nums[j])
            nums[i] = currMin
        return nums[0]
