# Problem: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string
# Runtime: 8 ms

class Solution:
    def minOperations(self, s: str) -> int:
        op1 = 0
        op2 = 0

        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == "0":
                    op1 += 1
                else:
                    op2 += 1
            else:
                if c == "0":
                    op2 += 1
                else:
                    op1 += 1

        return min(op1, op2)