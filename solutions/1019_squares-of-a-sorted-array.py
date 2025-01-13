# Problem: https://leetcode.com/problems/squares-of-a-sorted-array
# Runtime: 141 ms

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([x ** 2 for x in nums])