# Problem: https://leetcode.com/problems/walking-robot-simulation
# Runtime: 39 ms

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacleSet = set()

        for ob in obstacles:
            obstacleSet.add((ob[0], ob[1]))

        x, y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIdx = 0
        maxDist = 0

        for c in commands:
            if c == -2:
                dirIdx = (dirIdx - 1) % len(directions)
                continue
            elif c == -1:
                dirIdx = (dirIdx + 1) % len(directions)
                continue
            for i in range(c):
                newX = x + directions[dirIdx][0]
                newY = y + directions[dirIdx][1]
                if (newX, newY) in obstacleSet:
                    break
                x, y = newX, newY
                maxDist = max(maxDist, x ** 2 + y ** 2)
        
        return maxDist