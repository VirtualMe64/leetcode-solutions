# Problem: https://leetcode.com/problems/walking-robot-simulation
# Runtime: 271 ms

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = (0, 1) # x, y
        pos = (0, 0)
        obstacleSet = set([(o[0], o[1]) for o in obstacles])

        maxDist = 0

        for command in commands:
            if command == -2:
                direction = (-direction[1], direction[0])
            if command == -1:
                direction = (direction[1], -direction[0])
            else:
                for i in range(command):
                    potentialPos = (pos[0] + direction[0], pos[1] + direction[1])
                    if potentialPos in obstacleSet:
                        break
                    pos = potentialPos
            maxDist = max(maxDist, pos[0] ** 2 + pos[1] ** 2)
        return maxDist