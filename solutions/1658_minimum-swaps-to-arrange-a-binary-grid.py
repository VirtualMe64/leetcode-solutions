# Problem: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid
# Runtime: 12 ms

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # on row i (0 indexed), rightmost zero index <= i
        # greedy solution may work (take closest that's valid)

        values = []
        for row in grid:
            lastOne = 0
            for i, v in enumerate(row):
                if v == 1:
                    lastOne = i
            values.append(lastOne)

        moves = 0

        for maxIdx in range(len(values)):
            for i, n in enumerate(values):
                if n <= maxIdx:
                    moves += i
                    values.pop(i)
                    break
            else:
                return -1
        
        return moves