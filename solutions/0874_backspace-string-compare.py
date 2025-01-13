# Problem: https://leetcode.com/problems/backspace-string-compare
# Runtime: 38 ms

class Solution:
    def constructString(self, s):
        out = ""
        endIdx = 0

        for c in s:
            if c == "#":
                endIdx = 0 if endIdx == 0 else endIdx - 1
            else:
                out = out[0:endIdx] + c
                endIdx += 1
        
        return out[0:endIdx]

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.constructString(s) == self.constructString(t)