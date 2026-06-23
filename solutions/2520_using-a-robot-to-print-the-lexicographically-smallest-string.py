# Problem: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string
# Runtime: 619 ms

class Solution:
    def robotWithString(self, s: str) -> str:
        cnts = {}
        for c in s:
            cnts[c] = cnts.get(c, 0) + 1
        
        options = sorted([x for x in cnts.keys()])

        out = ""
        optionsPtr = 0
        sPtr = 0
        stack = []

        while sPtr < len(s):
            if len(stack) == 0 or stack[-1] > options[optionsPtr][0]:
                cnts[s[sPtr]] -= 1
                while optionsPtr < len(options) and cnts[options[optionsPtr]] == 0:
                    optionsPtr += 1
                stack.append(s[sPtr])
                sPtr += 1

            else:
                out += stack.pop(-1)

        while len(stack) > 0:
            out += stack.pop(-1)
        
        return out