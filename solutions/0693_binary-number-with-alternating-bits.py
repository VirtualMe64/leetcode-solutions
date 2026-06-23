# Problem: https://leetcode.com/problems/binary-number-with-alternating-bits
# Runtime: 0 ms

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n > 0:
            if n % 2 == prev:
                return False
            prev = n % 2
            n >>= 1
        return True