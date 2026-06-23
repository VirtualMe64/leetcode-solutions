# Problem: https://leetcode.com/problems/robot-return-to-origin
# Runtime: 0 ms

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')