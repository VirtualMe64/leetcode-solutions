# Problem: https://leetcode.com/problems/reverse-integer
# Runtime: 38 ms

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (2 ** 31) - 1
        INT_MIN = -(2 ** 31)

        val = abs(x)
        out = 0
        while val > 0:
            out *= 10
            out += val % 10
            val = val // 10

        if out > INT_MAX or out < INT_MIN:
            return 0
        
        return out if x > 0 else -out