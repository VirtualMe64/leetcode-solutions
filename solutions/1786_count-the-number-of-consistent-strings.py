# Problem: https://leetcode.com/problems/count-the-number-of-consistent-strings
# Runtime: 221 ms

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set([c for c in allowed])

        valid = 0
        for w in words:
            valid += 1
            for c in w:
                if c not in allowedSet:
                    valid -= 1
                    break
        
        return valid