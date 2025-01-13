# Problem: https://leetcode.com/problems/permutations
# Runtime: 28 ms

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        out = []
        for index, val in enumerate(nums):
            rest = nums[0 : index] + nums[index + 1:]
            out.extend([[val] + l for l in self.permute(rest)])
        return out