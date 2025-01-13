# Problem: https://leetcode.com/problems/rotting-oranges
# Runtime: 75 ms

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # intuition: bfs
        # naive: bfs from each rotting orange
        # better: expand from frontier, take min
        frontier = []
        isFresh = False
        dists = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    frontier.append((row, col))
                    dists[row][col] = 0
                if grid[row][col] == 1:
                    isFresh = True

        if not isFresh:
            return 0
        
        def getNeighbors(row, col):
            for dRow, dCol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newRow = row + dRow
                newCol = col + dCol
                if newRow >= 0 and newCol >= 0 and \
                    newRow < len(grid) and newCol < len(grid[0]):
                    yield (newRow, newCol)

        while len(frontier) > 0:
            curr = frontier.pop(0)
            currDist = dists[curr[0]][curr[1]]
            for nbr in getNeighbors(*curr):
                gridVal = grid[nbr[0]][nbr[1]]
                distVal = dists[nbr[0]][nbr[1]]
                print(nbr, gridVal, distVal)

                if gridVal == 1 and distVal == -1:
                    frontier.append(nbr)
                    dists[nbr[0]][nbr[1]] = currDist + 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and dists[row][col] == -1:
                    return -1

        return max([max(x) for x in dists])