# Problem: https://leetcode.com/problems/smallest-number-with-all-set-bits
# Runtime: 0 ms

class Solution:
    def smallestNumber(self, n: int) -> int:
        base = 1
        while base <= n:
            base *= 2
        return base - 1 