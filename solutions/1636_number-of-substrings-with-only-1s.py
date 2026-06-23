# Problem: https://leetcode.com/problems/number-of-substrings-with-only-1s
# Runtime: 15 ms

MOD = 10 ** 9 + 7

class Solution:
    def numSub(self, s: str) -> int:
        length = 0
        total = 0

        for c in s:
            if c == '1':
                length += 1
            elif length > 0:
                total += (length * (length + 1)) >> 1
                total %= MOD
                length = 0
        
        if length > 0:
            total += (length * (length + 1)) >> 1
            total %= MOD
        
        return total