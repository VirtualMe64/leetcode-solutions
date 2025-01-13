# Problem: https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid
# Runtime: 387 ms

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        inYCounts = [0 for i in range(3)]
        outYCounts = [0 for i in range(3)]

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                bottomY = j == len(grid) // 2
                topY = i == j or i + j + 1 == len(grid)
                bottom = i > len(grid) // 2

                inY = bottomY if bottom else topY
                if inY:
                    inYCounts[val] += 1
                else:
                    outYCounts[val] += 1
        
        total = len(grid) ** 2

        best = None

        for i in range(3): # num used to fill in y
            for j in range(3): # num used to fill in rest
                if i != j:
                    val = total - inYCounts[i] - outYCounts[j]
                    best = min(best, val) if best != None else val
        
        return best