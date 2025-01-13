# Problem: https://leetcode.com/problems/consecutive-numbers-sum
# Runtime: 23 ms

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # a integers starting at b:
        # ab + ((a^2 - a) /2) = n
        # (a^2 - a + 2ab) / 2 = n
        # a^2 - a + 2ab = 2n
        # a(a - 1 + 2b) = 2n

        # for a given a, we can make 2n if 2n/a has opposite parity of a, a^2 - a <= 2n

        base = 2 * n
        factors = 1
        for factor in range(2, int(base ** 0.5) + 1):
            if base % factor != 0:
                continue
            rem = base // factor
            if rem & 1 != factor & 1:
                factors += 1
        return factors