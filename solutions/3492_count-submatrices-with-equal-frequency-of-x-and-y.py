# Problem: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y
# Runtime: 349 ms

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        dp = [[0, 0] for i in range(len(grid[0]))] # x count, y count
        out = 0

        for row in grid:
            currX = 0
            currY = 0
            for i, val in enumerate(row):
                if val == "X":
                    currX += 1
                elif val == "Y":
                    currY += 1
                dp[i][0] += currX
                dp[i][1] += currY
                if dp[i][0] == dp[i][1] and dp[i][0] > 0:
                    out += 1
        
        return out