# Problem: https://leetcode.com/problems/number-of-islands
# Runtime: 295 ms

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        queue = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        numIslands = 0
        islandMap = {}
        while len(queue) > 0:
            curr = queue.pop()

            if curr in visited:
                continue

            if grid[curr[0]][curr[1]] == "1":
                visited.add(curr)
                if curr not in islandMap:
                    numIslands += 1
                    islandMap[curr] = numIslands

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nbr = (curr[0] + dx, curr[1] + dy)
                    if nbr[0] < 0 or nbr[0] >= len(grid) or nbr[1] < 0 or nbr[1] >= len(grid[0]):
                        continue
                    if grid[nbr[0]][nbr[1]] == "1":
                        islandMap[nbr] = islandMap[curr]
                        queue.append(nbr)
        
        return numIslands