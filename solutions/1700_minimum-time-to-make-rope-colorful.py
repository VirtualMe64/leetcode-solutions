# Problem: https://leetcode.com/problems/minimum-time-to-make-rope-colorful
# Runtime: 75 ms

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        prevColor = None
        streakLen = 0
        streakMax = 0
        streakTot = 0

        for color, time in zip(colors, neededTime):
            if color != prevColor:
                if streakLen > 1:
                    total += streakTot - streakMax
                streakLen = 1
                streakMax = time
                streakTot = time
            else:
                streakLen += 1
                streakMax = max(streakMax, time)
                streakTot += time

            prevColor = color
        
        if streakLen > 1:
            total += streakTot - streakMax
        
        return total