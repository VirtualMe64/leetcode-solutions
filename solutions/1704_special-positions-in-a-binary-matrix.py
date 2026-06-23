# Problem: https://leetcode.com/problems/special-positions-in-a-binary-matrix
# Runtime: 11 ms

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row1Counts = [0 for _ in range(len(mat))]
        col1Counts = [0 for _ in range(len(mat[0]))]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    row1Counts[row] += 1
                    col1Counts[col] += 1

        total = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1 and row1Counts[row] == 1 and col1Counts[col] == 1:
                    total += 1
        return total