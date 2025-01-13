# Problem: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings
# Runtime: 243 ms

class Solution:
    def recurse(self, s, seen):
        if len(s) == 0:
            return 0
        copy = [x for x in seen]
        best = 0
        for l in range(1, len(s) + 1):
            substr = s[0:l]
            if substr not in seen:
                val = self.recurse(s[l:], copy + [substr]) + 1
            else:
                continue
            best = max(best, val) 

        return best

    def maxUniqueSplit(self, s: str) -> int:
        return self.recurse(s, [])