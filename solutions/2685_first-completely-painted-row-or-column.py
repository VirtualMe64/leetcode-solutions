# Problem: https://leetcode.com/problems/first-completely-painted-row-or-column
# Runtime: 127 ms

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        numMap = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                numMap[mat[i][j]] = (i, j)

        colCnts = [0 for _ in range(len(mat))]
        rowCnts = [0 for _ in range(len(mat[0]))]

        for i, num in enumerate(arr):
            col, row = numMap[num]
            colCnts[col] += 1
            if colCnts[col] >= len(mat[0]):
                return i
            rowCnts[row] += 1
            if rowCnts[row] >= len(mat):
                return i