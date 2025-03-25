# Problem: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections
# Runtime: 115 ms

import bisect

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        for order in [0, 1]: # first sort horizontally, then vertically
            sortedRects = sorted(rectangles, key = lambda x : x[order])
            currGaps = 0
            currEnd = 0
            for rect in sortedRects:
                v1 = rect[0 + order]
                v2 = rect[2 + order]

                if v2 < currEnd: # already contained in cut
                    continue
                if v1 < currEnd: # need to extend the cut
                    currEnd = v2
                else: # start a new cut!
                    currGaps += 1
                    currEnd = v2
                
                if currGaps >= 3:
                    return True
            
        return False

