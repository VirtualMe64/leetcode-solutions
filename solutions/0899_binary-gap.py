# Problem: https://leetcode.com/problems/binary-gap
# Runtime: 0 ms

class Solution:
    def binaryGap(self, n: int) -> int:
        last = None
        best = 0

        i = 0
        while n > 0:
            i += 1
            c = n % 2
            n = n >> 1

            if c == 1:
                if last is not None:
                    best = max(best, i - last)
                last = i
    
        return best