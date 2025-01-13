# Problem: https://leetcode.com/problems/delete-characters-to-make-fancy-string

class Solution:
    def makeFancyString(self, s: str) -> str:
        out = ""
        count = 1
        prev = ""

        for c in s:
            if c == prev:
                count += 1
            else:
                count = 1
            if count < 3:
                out += c
            prev = c
        
        return out