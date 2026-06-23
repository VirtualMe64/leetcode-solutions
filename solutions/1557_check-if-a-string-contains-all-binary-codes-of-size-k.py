# Problem: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k
# Runtime: 263 ms

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique = set()
        curr = 0

        if 2 ** k > len(s):
            return False

        for i, c in enumerate(s):
            curr <<= 1
            curr += 1 if c == '1' else 0
            curr = curr % (2 ** k)

            if i + 1 >= k:
                unique.add(curr)
            
            if len(unique) == 2 ** k:
                return True
        
        return False