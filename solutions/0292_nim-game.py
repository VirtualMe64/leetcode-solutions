# Problem: https://leetcode.com/problems/nim-game
# Runtime: 0 ms

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0