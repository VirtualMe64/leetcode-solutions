# Problem: https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap
# Runtime: 41 ms

class Solution:
    def getSmallestString(self, s: str) -> str:
        # want highest swap
        last = s[0]
        for i, char in enumerate(s[1:]):
            if (ord(last) + ord(char)) % 2 == 0: # same parity
                if char < last: # larger
                    return s[0:i] + char + last + s[i + 2:]    
            last = char
        return s