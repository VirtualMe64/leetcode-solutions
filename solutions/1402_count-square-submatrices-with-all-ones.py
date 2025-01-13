# Problem: https://leetcode.com/problems/count-square-submatrices-with-all-ones
# Runtime: 69 ms

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        width = len(matrix[0])
        height = len(matrix)

        dp = [[0 for i in range(width)] for j in range(height)]
        count = 0

        for y in range(height):
            for x in range(width):
                val = matrix[y][x]
                if val == 0:
                    continue
                left = dp[y][x - 1] if x > 0 else 0
                up = dp[y - 1][x] if y > 0 else 0
                diag = dp[y - 1][x - 1] if (x > 0 and y > 0) else 0

                squares = min(left, up, diag) + 1
                count += squares
                dp[y][x] = squares
        
        return count