# Problem: https://leetcode.com/problems/divide-two-integers
# Runtime: 0 ms

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return dividend

        # note sign than use abs to only consider positive numbers
        negative = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        # idea: see if decreasing multiples of 2 fit
        out = 0

        # test from 2^31 to 2^0
        for shift in range(31, -1, -1):
            shifted_divisor = divisor << shift
            if (shifted_divisor) <= dividend:
                out += 1 << shift
                dividend -= (shifted_divisor)
        
        # handle lower limit for 32 bit integers with min
        return -out if negative else min(out, 2147483647)