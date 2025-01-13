# Problem: https://leetcode.com/problems/snake-in-matrix
# Runtime: 65 ms

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        val = 0
        for command in commands:
            if command == "UP":
                val -= n
            if command == "RIGHT":
                val += 1
            if command == "LEFT":
                val -= 1
            if command == "DOWN":
                val += n
        return val