# Problem: https://leetcode.com/problems/count-unguarded-cells-in-the-grid
# Runtime: 837 ms

from bisect import bisect_left

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guardSet = set([(r, c) for r, c in guards])
        wallSet = set([(r, c) for r, c in walls])

        rowUnguarded = set()
        colUnguarded = set()

        # first, find row unguarded cells (with 2 pointer)
        for row in range(m):
            leftUnguarded = True
            rightUnguarded = False

            ptr1 = -1
            ptr2 = -1

            currPtr = 2 # ptr2

            while ptr1 < n:
                if currPtr == 2:
                    ptr2 += 1
                    if (row, ptr2) in guardSet:
                        rightUnguarded = False
                        currPtr = 1
                    elif (row, ptr2) in wallSet or ptr2 == n:
                        rightUnguarded = True
                        currPtr = 1
                else:
                    ptr1 += 1
                    if ptr1 == ptr2:
                        leftUnguarded = rightUnguarded
                        currPtr = 2
                    else:
                        if leftUnguarded and rightUnguarded:
                            rowUnguarded.add((row, ptr1))
        
        # next, find col unguarded cells
        for col in range(n):
            leftUnguarded = True
            rightUnguarded = False

            ptr1 = -1
            ptr2 = -1

            currPtr = 2 # ptr2

            while ptr1 < m:
                if currPtr == 2:
                    ptr2 += 1
                    if (ptr2, col) in guardSet:
                        rightUnguarded = False
                        currPtr = 1
                    elif (ptr2, col) in wallSet or ptr2 == m:
                        rightUnguarded = True
                        currPtr = 1
                else:
                    ptr1 += 1
                    if ptr1 == ptr2:
                        leftUnguarded = rightUnguarded
                        currPtr = 2
                    else:
                        if leftUnguarded and rightUnguarded:
                            colUnguarded.add((ptr1, col))
        
        return len(rowUnguarded.intersection(colUnguarded))