# Problem: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful
# Runtime: 31 ms

class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        runtype = ''
        for i, c in enumerate(s):
            if i % 2 == 0:
                runtype = c
            else:
                if c != runtype:
                    changes += 1
        return changes