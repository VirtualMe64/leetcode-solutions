# Problem: https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i
# Runtime: 2946 ms

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minX = None
        minY = None
        maxX = None
        maxY = None
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    minX = min(minX, x) if minX != None else x
                    minY = min(minY, y) if minY != None else y
                    maxX = max(maxX, x) if maxX != None else x
                    maxY = max(maxY, y) if maxY != None else y
                    
                    # print(y, x)
                    # print(minX, minY, maxX, maxY)    
                    
        if minX == None:
            return 0
    
        return (maxY - minY + 1) * (maxX - minX + 1)