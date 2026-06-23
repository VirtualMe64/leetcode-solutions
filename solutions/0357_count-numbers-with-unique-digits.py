# Problem: https://leetcode.com/problems/count-numbers-with-unique-digits
# Runtime: 38 ms

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        total = 1; # for 0
        for i in range(1, n + 1):
            # i is length
            curr = 9
            for j in range(1, i):
                curr *= 10 - j
            total += curr
        return total