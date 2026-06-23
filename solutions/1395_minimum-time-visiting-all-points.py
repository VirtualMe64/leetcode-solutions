# Problem: https://leetcode.com/problems/minimum-time-visiting-all-points
# Runtime: 1 ms

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        lastPoint = points[0]
        total = 0

        for p in points[1:]:
            dx = abs(p[0] - lastPoint[0])
            dy = abs(p[1] - lastPoint[1])

            diff = abs(dx - dy)
            diag = min(dx, dy)
            total += diff + diag

            lastPoint = p
        
        return total