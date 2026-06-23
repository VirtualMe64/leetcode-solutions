# Problem: https://leetcode.com/problems/champagne-tower
# Runtime: 110 ms

import math

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp, actualize each row

        currRow = [poured]

        for _ in range(query_row):
            newRow = [0 for i in range(len(currRow) + 1)]
            for i, v in enumerate(currRow):
                overflow = max(v - 1, 0)
                newRow[i] += overflow / 2
                newRow[i + 1] += overflow / 2

            currRow = newRow
        
        return min(currRow[query_glass], 1)