# Problem: https://leetcode.com/problems/check-balanced-string
# Runtime: 3 ms

class Solution:
    def isBalanced(self, num: str) -> bool:
        evenTotal = 0
        oddTotal = 0

        for i, c in enumerate(num):
            val = int(c)
            if i % 2 == 0:
                evenTotal += val
            else:
                oddTotal += val

        return evenTotal == oddTotal