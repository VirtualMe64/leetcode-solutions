# Problem: https://leetcode.com/problems/number-of-zigzag-arrays-i
# Runtime: 7863 ms

MOD = 10 ** 9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # idea: dp of some sort
        # dp[d][x][i] is number of solutions for:
        #   array of length i
        #   ending in x
        #   where previous two elements are d = {0 if ascending, 1 if descending}
        # complexity: 3 * n * (l - r) cells
        # naive filling would take 2 * n * (l - r) for each cell -- too inefficient!
        # i think we can keep a running sum and do it smarter

        # recurrence:
        # dp[ascending][x][i] = sum_(x' < x)(dp[descending][x'][i - 1])
        # dp[descending][x][i] = sum_(x' > x)(dp[ascending][x'][i - 1])

        # start with n = 2 and analytically compute values
        # asc = number of entries less than x (x - l)
        # desc = number of values > x (r - x)
        # not actualizing the i dimension since we only need i - 1
        # using convention that first entry corresponds to x = l
        dp_asc = [x - l for x in range(l, r + 1)]
        dp_dsc = [r - x for x in range(l, r + 1)]

        for _ in range(n - 2):
            dp_asc_upper = sum(dp_asc)
            dp_dsc_lower = 0

            for x in range(r - l + 1):
                # load current value before it's overwritten
                dp_asc_val = dp_asc[x]
                dp_dsc_val = dp_dsc[x]

                dp_asc_upper -= dp_asc_val

                # dp[ascending][x][i] = sum_(x' < x)(dp[descending][x'][i - 1])
                dp_asc[x] = dp_dsc_lower % MOD

                # dp[descending][x][i] = sum_(x' > x)(dp[ascending][x'][i - 1])
                dp_dsc[x] = dp_asc_upper % MOD

                dp_dsc_lower += dp_dsc_val

        return (sum(dp_asc) + sum(dp_dsc)) % MOD