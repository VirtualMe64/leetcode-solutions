# Problem: https://leetcode.com/problems/surrounded-regions
# Runtime: 116 ms

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        Idea: DFS just on edge items -- replace all that need to be flipped
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][m - 1] == 'O':
                self.dfs(board, i, m - 1)
        
        for i in range(m):
            if board[0][i] == 'O':
                self.dfs(board, 0, i)
            if board[n - 1][i] == 'O':
                self.dfs(board, n - 1, i)
        
        for i in range(n):
            for j in range(m):
                curr = board[i][j]
                if curr == 'T':
                    board[i][j] = 'O'
                if curr == 'O':
                    board[i][j] = 'X'

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return
        if board[i][j] != 'O':
            return
        board[i][j] = 'T'
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)