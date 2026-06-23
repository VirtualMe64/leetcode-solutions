# Problem: https://leetcode.com/problems/process-string-with-special-operations-i
# Runtime: 107 ms

from collections import deque

class Solution:
    def processStr(self, s: str) -> str:
        out = deque()

        for c in s:
            if c == "*":
                if len(out) > 0:
                        out.pop()
            elif c == "#":
                out.extend(out)
            elif c == "%":
                out.reverse()
            else:
                out.append(c)

        return "".join(out)