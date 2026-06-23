# Problem: https://leetcode.com/problems/4sum
# Runtime: 8174 ms

from functools import cache

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        cnts = {}
        for n in nums:
            cnts[n] = cnts.get(n, 0) + 1
        nums = []
        for n, c in cnts.items():
            nums.extend([n] * min(4, c))

        out = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            out.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
            
        return [list(q) for q in out]