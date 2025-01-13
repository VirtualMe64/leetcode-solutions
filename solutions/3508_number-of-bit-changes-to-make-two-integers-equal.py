# Problem: https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal
# Runtime: 31 ms

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        changes = 0
        while k > 0 or n > 0:
            nBit = n & 1
            kBit = k & 1
            
            if nBit and not kBit:
                changes += 1
            if kBit and not nBit:
                return -1
            
            n = n >> 1
            k = k >> 1
        return changes