# Problem: https://leetcode.com/problems/reverse-bits
# Runtime: 32 ms

class Solution:
    def reverseBits(self, n: int) -> int:
        bitcount = 31
        out = 0

        while n > 0:
            if n % 2 == 1:
                out += 1 << bitcount
            n = n // 2
            bitcount -= 1
        return out