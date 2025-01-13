# Problem: https://leetcode.com/problems/maximum-number-of-points-with-cost
# Runtime: 1571 ms

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # idea: iterate through one row at a time, finding point values
        # take difference from previous to get max
        # O(m * n * n)

        # [2 2 2]

        prev = points[0]

        for row in points[1:]:
            curr = []
            bests = getRowOptimals(prev)
            for i, pt in enumerate(row):
                best = bests[i]
                curr.append(pt + best)
            prev = curr

        return max(prev)

# Given a list (row) of points, returns the max point option for a point in the next row at each index
def getRowOptimals(row):
    best = [None for _ in range(len(row))]

    curr = None
    best[0] = row[0]

    
    # step 1: forward pass
    for i, val in enumerate(row[1::]):
        idx = i + 1
        best[idx] = max(best[idx - 1] - 1, val)

    best[-1] = max(best[-1], row[-1])
    # step 2: backwards pass
    for i, val in enumerate(row[::-1][1::]):
        idx = len(row) - i - 2
        best[idx] = max(best[idx], best[idx + 1] - 1, val)

    return best