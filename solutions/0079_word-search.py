# Problem: https://leetcode.com/problems/word-search
# Runtime: 7544 ms

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        target = word[0]

        frontier = []

        for row, arr in enumerate(board):
            for col, letter in enumerate(arr):
                if letter == target:
                    frontier.append((1, (row, col), []))
        
        def getNeighbors(square, parents):
            for dRow, dCol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newSquare = (square[0] + dRow, square[1] + dCol)
                if newSquare[0] >= 0 and newSquare[0] < len(board):
                    if newSquare[1] >= 0 and newSquare[1] < len(board[0]):
                        if newSquare not in parents:
                            yield newSquare

        # DFS
        while len(frontier) > 0:
            curr_len, curr_loc, parents = frontier.pop()
            if curr_len == len(word):
                return True

            target = word[curr_len]
            for neighbor in getNeighbors(curr_loc, parents):
                if board[neighbor[0]][neighbor[1]] == target:
                    frontier.append((curr_len + 1, neighbor, parents + [curr_loc]))

        return False
    