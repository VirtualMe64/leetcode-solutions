# Problem: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k
# Runtime: 115 ms

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        dp = [0 for _ in range(len(grid[0]))]

        out = 0
        for row in grid:
            currSum = 0

            if dp[0] > k:
                break

            for i, v in enumerate(row):
                currSum += v
                dp[i] += currSum
                if dp[i] <= k:
                    out += 1
                else:
                    break
        
        return out