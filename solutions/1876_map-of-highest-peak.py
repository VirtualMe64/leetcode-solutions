# Problem: https://leetcode.com/problems/map-of-highest-peak
# Runtime: 2531 ms

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # it's giving bfs
        heights = [[None for i in range(len(isWater[0]))] for j in range(len(isWater))]
        queue = []
        visited = set()

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]:
                    queue.append((i, j))
                    visited.add((i, j))
                    heights[i][j] = 0

        oob = lambda i, j : i < 0 or j < 0 or i >= len(isWater) or j >= len(isWater[0]) 
        nbr = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        idx = 0

        while len(queue) > idx:
            (i, j) = queue[idx]
            idx += 1

            minNbr = None

            for dx, dy in nbr:
                if oob(i + dx, j + dy):
                    continue
                nbrHeight = heights[i + dx][j + dy]
                if nbrHeight is not None:
                    minNbr = nbrHeight if minNbr is None else min(minNbr, nbrHeight)
                if (i + dx, j + dy) not in visited:
                    queue.append((i + dx, j + dy))
                    visited.add((i + dx, j + dy))

            heights[i][j] = 0 if isWater[i][j] else minNbr + 1
        
        return heights