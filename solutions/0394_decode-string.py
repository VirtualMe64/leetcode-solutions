# Problem: https://leetcode.com/problems/decode-string
# Runtime: 37 ms

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        currString = ""
        currInt = ""
        for c in s:
            # print(c, currString, currInt, stack)
            if c.isdigit():
                currInt += c
            elif c == '[':
                stack.append((int(currInt), len(currString)))
                currInt = ""
            elif c == ']':
                repititions, startIdx = stack.pop(-1)
                currString += (repititions - 1) * currString[startIdx:]
            else:
                currString += c

        return currString