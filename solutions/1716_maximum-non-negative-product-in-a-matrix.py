# Problem: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix
# Runtime: 7 ms

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # max pos magnitude, max neg magnitude, zero?
        dp = [[None, None, False] for i in range(len(grid[0]))]
        first = grid[0][0]
        if first > 0:
            dp[0] = [first, None, False]
        elif first < 0:
            dp[0] = [None, first, False]
        else:
            dp[0] = [None, None, True]

        def update(old, newValues):
            negVals = [v for v in newValues if v < 0]
            nonNegVals = [v for v in newValues if v > 0]

            out = []
            if len(nonNegVals) > 0:
                out.append(max(nonNegVals))
            else:
                out.append(None)
    
            if len(negVals) > 0:
                out.append(min(negVals))
            else:
                out.append(None)
            
            out.append(old[2] or 0 in newValues)
            
            return out


        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                newVals = []
                if i > 0:
                    base = dp[j]
                    if base[0] is not None:
                        newVals.append(v * base[0])
                    if base[1] is not None:
                        newVals.append(v * base[1])
                    if base[2]:
                        newVals.append(0)
                if j > 0:
                    base = dp[j - 1]
                    if base[0] is not None:
                        newVals.append(v * base[0])
                    if base[1] is not None:
                        newVals.append(v * base[1])
                    if base[2]:
                        newVals.append(0)
                if i > 0 or j > 0:
                    dp[j] = update(dp[j], newVals)
            # print(dp)

        if dp[-1][0] is None:
            return 0 if dp[-1][2] else -1
        return dp[-1][0] % (10 ** 9 + 7)