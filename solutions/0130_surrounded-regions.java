// Problem: https://leetcode.com/problems/surrounded-regions
// Runtime: 5 ms

class Solution {
    public void solve(char[][] board) {
        boolean[][] visited = new boolean[board.length][board[0].length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 'O' && !visited[i][j]) {
                    boolean surrounded = dfs(board, visited, i, j, true);
                    if (surrounded) {
                        flip(board, i, j);
                    }
                }
            }
        }
    }

    // return if the square is part of a group that's surrounded
    private boolean dfs(char[][] board, boolean[][] visited, int i, int j, boolean surrounded) {
        // check if square is of the edge
        if (i < 0 || j < 0 || i == board.length || j == board[0].length) {
            return false;
        }
        if (visited[i][j] || board[i][j] == 'X') {
            return true;
        }
        visited[i][j] = true;
        // check all 4 directions
        surrounded &= dfs(board, visited, i + 1, j, surrounded);
        surrounded &= dfs(board, visited, i - 1, j, surrounded);
        surrounded &= dfs(board, visited, i, j + 1, surrounded);
        surrounded &= dfs(board, visited, i, j - 1, surrounded);

        return surrounded;
    }

    private void flip(char[][] board, int i, int j) {
        if (i < 0 || j < 0 || i == board.length || j == board[0].length || board[i][j] == 'X') {
            return;
        }
        board[i][j] = 'X';

        flip(board, i + 1, j);
        flip(board, i - 1, j);
        flip(board, i, j + 1);
        flip(board, i, j - 1);
    }
}
/*
["O","O","O","O","X","X"],
["O","O","O","O","O","O"],
["O","X","O","X","O","O"],
["O","X","O","O","X","O"],
["O","X","O","X","O","O"],
["O","X","O","O","O","O"]
*/