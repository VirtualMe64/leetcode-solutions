# Problem: https://leetcode.com/problems/divide-array-into-equal-pairs
# Runtime: 5 ms

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnts = {}
        for n in nums:
            cnts[n] = cnts.get(n, 0) + 1
        for val in cnts.values():
            if val % 2 == 1:
                return False
        return True