# Problem: https://leetcode.com/problems/valid-sudoku
# Runtime: 3 ms

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sets = [set() for _ in range(27)]
        posToSets = lambda i, j: [i, 9 + j, 18 + (3 * (i // 3)) + ((j // 3) % 3)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                for setIdx in posToSets(i, j):
                    if val in sets[setIdx]:
                        return False
                    sets[setIdx].add(val)
        
        return True