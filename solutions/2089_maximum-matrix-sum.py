# Problem: https://leetcode.com/problems/maximum-matrix-sum
# Runtime: 84 ms

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        minAbs = abs(matrix[0][0])
        isZero = False
        numNeg = 0

        for row in matrix:
            for val in row:
                total += abs(val)
                minAbs = min(minAbs, abs(val))
                if val < 0:
                    numNeg += 1

        if numNeg % 2 == 0:
            return total
        else:
            return total + -(2 * minAbs)