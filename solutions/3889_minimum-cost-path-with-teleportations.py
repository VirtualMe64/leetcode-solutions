# Problem: https://leetcode.com/problems/minimum-cost-path-with-teleportations
# Runtime: 3433 ms

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # step 1: min cost to get to any square using only normal moves
        costs = [[float('inf') for i in range(len(grid[0]))] for j in range(len(grid))]
        costs[0][0] = 0
        # sorted locations will be helpful for teleportation step
        locs = []
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                locs.append((i, j))

        def normalStep():
            for i in range(len(grid[0])):
                for j in range(len(grid)):
                    leftOption = costs[j][i - 1] + grid[j][i] if i > 0 else float('inf')
                    upOption = costs[j - 1][i] + grid[j][i] if j > 0 else float('inf')
                    currOption = costs[j][i]

                    val = min(leftOption, upOption, currOption)
                    costs[j][i] = val

        def teleportStep():
            # keep track of currently seen min
            # since we look at indices from largest to lowest, we can teleport from any previously seen
            locs.sort(reverse=True, key = lambda x : (grid[x[1]][x[0]], -costs[x[1]][x[0]]))
            minCost = float('inf')
            for i, j in locs:
                currCost = costs[j][i]
                if currCost < minCost:
                    minCost = currCost
                else:
                    costs[j][i] = minCost
            
        normalStep()
        for i in range(k):
            teleportStep()
            normalStep()

        return costs[-1][-1]