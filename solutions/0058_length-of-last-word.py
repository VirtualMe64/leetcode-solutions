# Problem: https://leetcode.com/problems/length-of-last-word
# Runtime: 36 ms

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curr = 0
        firstC = False
        for c in s[::-1]:
            if c == ' ':
                if firstC:
                    return curr
            else:
                curr += 1
                firstC = True
        return curr