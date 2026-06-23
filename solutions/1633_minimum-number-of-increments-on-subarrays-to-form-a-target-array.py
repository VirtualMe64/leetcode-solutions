# Problem: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array
# Runtime: 74 ms

from bisect import bisect_left

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        out = 0
        last = 0

        for n in target:
            out += max(n - last, 0)
            last = n
        
        return out