# Problem: https://leetcode.com/problems/count-number-of-trapezoids-ii
# Runtime: 1329 ms

import math

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # iterate over every pair of points
        # for each slope, store count by y intercept
        # total is running multiplication
        # problem: every rhombus will be double counted!
        # solution: materialize every trapezoid, check for rhombuses?
        # observation: rhombuses mean parallelogram with same length between pts
        # if rhombus found, take note and subtract out after (// 2 since double counted)
        # to find rhombuses efficiently, keep track of norm count for each y-int

        results = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                if p2[0] < p1[0] or (p2[0] == p1[0] and p2[1] < p1[1]): # canonical order
                    p1, p2 = p2, p1

                raw_dy = p1[1] - p2[1]
                raw_dx = p1[0] - p2[0]
                g = math.gcd(raw_dy, raw_dx)
                dy = raw_dy // g
                dx = raw_dx // g
                norm = raw_dy ** 2 + raw_dx ** 2
                slope = (dx, dy)
                intercept = dx * points[i][1] - dy * points[i][0] # floating point safe
            
                slopeDict = results.get(slope, {})
                intDict = slopeDict.get(intercept, {})
                intDict[norm] = intDict.get(norm, 0) + 1
                slopeDict[intercept] = intDict
                results[slope] = slopeDict

        total = 0
        rhombusCnt = 0
        for slopeDict in results.values():
            running = 0
            runningByNorm = {}

            for intDict in slopeDict.values():
                intTotal = 0
                for norm, cnt in intDict.items():
                    intTotal += cnt
                    rhombusCnt += cnt * runningByNorm.get(norm, 0)
                    runningByNorm[norm] = runningByNorm.get(norm, 0) + cnt

                total += running * intTotal
                running += intTotal

        return total - rhombusCnt // 2