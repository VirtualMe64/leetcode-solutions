# Problem: https://leetcode.com/problems/largest-submatrix-with-rearrangements
# Runtime: 177 ms

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # for each row, what runs end at that row for each column (ignoring 0s)
        byRow = {i : [] for i in range(len(matrix))}
        for col in range(len(matrix[0])):
            currRun = 0
            for row in range(len(matrix)):
                if matrix[row][col] == 1:
                    currRun += 1
                    byRow[row].append(currRun)
                else:
                    currRun = 0
        
        best = 0
        for row in byRow.values():
            # find max submatrix with bottom being that row
            row.sort(reverse=True)
            for i, v in enumerate(row):
                # since all i previous values were >= v, we can make submatrix size (i + 1) * v
                val = (i + 1) * v
                best = max(best, val)
    
        return best