# Problem: https://leetcode.com/problems/maximize-area-of-square-hole-in-grid
# Runtime: 1 ms

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        maxHori = 0
        prev = 0
        runLen = 0
        for h in hBars:
            if h == prev + 1:
                runLen += 1
            else:
                runLen = 1
            prev = h
            maxHori = max(maxHori, runLen)

        maxVerti = 0
        prev = 0
        runLen = 0
        for v in vBars:
            if v == prev + 1:
                runLen += 1
            else:
                runLen = 1
            prev = v
            maxVerti = max(maxVerti, runLen)

        return min(maxHori + 1, maxVerti + 1) ** 2