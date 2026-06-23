# Problem: https://leetcode.com/problems/detect-cycles-in-2d-grid
# Runtime: 475 ms

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()

        def explore(x, y, parent = None):
            # returns true if a cycle is detected
            visited.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x + dx, y + dy
                # check bounds
                if newX < 0 or newX >= len(grid[0]):
                    continue
                if newY < 0 or newY >= len(grid):
                    continue
                # no backtracking
                if (newX, newY) == parent:
                    continue
                # can only path through same value
                if grid[newY][newX] != grid[y][x]:
                    continue
                if (newX, newY) in visited:
                    # cycle detected!
                    return True
                if explore(newX, newY, (x, y)):
                    # cycle detected!
                    return True

            return False

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (x, y) not in visited:
                    if explore(x, y):
                        return True
        
        return False