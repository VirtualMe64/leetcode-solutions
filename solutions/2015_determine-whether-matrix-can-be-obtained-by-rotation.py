# Problem: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
# Runtime: 0 ms

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(target)
        def rot90(x, y): return y, n - x - 1 
        
        def checkRot(r):
            for x in range(n):
                for y in range(n):
                    nx, ny = x, y
                    for i in range(r):
                        nx, ny = rot90(nx, ny)
                    if mat[ny][nx] != target[y][x]:
                        return False
            return True

        for r in [0, 1, 2, 3]:
            if checkRot(r):
                return True
        return False