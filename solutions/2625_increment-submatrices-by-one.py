# Problem: https://leetcode.com/problems/increment-submatrices-by-one
# Runtime: 136 ms

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        out = [[0 for i in range(n)] for j in range(n)]

        for row1, col1, row2, col2 in queries:
            row2Edge = row2 + 1 >= n
            col2Edge = col2 + 1 >= n

            out[row1][col1] += 1
            if not row2Edge:
                out[row2 + 1][col1] -= 1
            if not col2Edge:
                out[row1][col2 + 1] -= 1
            if not col2Edge and not row2Edge:
                out[row2 + 1][col2 + 1] += 1

        rowCopy = [0 for i in range(n)]

        for row in range(n):
            acc = 0
            for col in range(n):
                rowCopy[col] += out[row][col]
                acc += rowCopy[col]
                out[row][col] = acc

        return out