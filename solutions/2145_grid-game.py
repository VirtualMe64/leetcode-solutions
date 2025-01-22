# Problem: https://leetcode.com/problems/grid-game
# Runtime: 93 ms

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # suppose robot 1 goes down at index i
        # robot b either gets all uppers after i or all lowers before i
        # so score(i) = max(lowers before i, uppers after i)
        # find min of score
        # precompute array sums to speed up computation
        upperTotal = sum(grid[0])
        currUpper = upperTotal - grid[0][0]
        currLower = 0

        robot1Score = currUpper
        for i in range(len(grid[0]) - 1):
            currUpper -= grid[0][i + 1]
            currLower += grid[1][i]

            robot2Score = max(currUpper, currLower)
            robot1Score = min(robot1Score, robot2Score)
        return robot1Score