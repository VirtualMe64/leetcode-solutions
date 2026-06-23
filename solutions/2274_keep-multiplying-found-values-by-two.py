# Problem: https://leetcode.com/problems/keep-multiplying-found-values-by-two
# Runtime: 2 ms

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numSet = set(nums)

        while original in nums:
            original *= 2
        
        return original