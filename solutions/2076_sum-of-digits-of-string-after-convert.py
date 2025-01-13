# Problem: https://leetcode.com/problems/sum-of-digits-of-string-after-convert
# Runtime: 29 ms

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        if s == '':
            return 0
        base = "".join([str(ord(c) - ord('a') + 1) for c in s])
        
        out = base
        for i in range(k):
            total = 0
            for c in out:
                total += ord(c) - ord('0')
            out = str(total)
        return int(out)