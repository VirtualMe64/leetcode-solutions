# Problem: https://leetcode.com/problems/maximum-height-of-a-triangle
# Runtime: 34 ms

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # for first color, n rows of that color costs: b = n^2
        # for second color, n rows of that color costs: b = n^2 + 1 =>
        if red == 0 and blue == 0:
            return 0
        
        for rows in range(30):
            firstRows = (rows + 1) // 2
            secondRows = rows // 2
            
            firstReq = firstRows ** 2
            secondReq = secondRows ** 2 + secondRows
            
            if (red >= firstReq and blue >= secondReq) or (blue >= firstReq and red >= secondReq):
                continue
            return rows - 1