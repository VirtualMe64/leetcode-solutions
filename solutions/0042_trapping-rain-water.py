# Problem: https://leetcode.com/problems/trapping-rain-water
# Runtime: 21 ms

import bisect

class Solution:
    def trap(self, height: List[int]) -> int:
        # step 1: find 'dead end'
        # a dead end is an index where every future index is lower

        heightWithIdx = sorted([(h, i) for i, h in enumerate(height)], reverse=True)

        deadEnds = [heightWithIdx[0][1]]  # stored indices of dead ends
        last = heightWithIdx[0]
        for h, i in heightWithIdx[1:]:
            if last[0] != h and i > deadEnds[-1]:
                deadEnds.append(i)
            last = (h, i)
        dePtr = 0
        total = 0
        leftWall = 0

        for i, h in enumerate(height):
            if deadEnds[dePtr] == i:
                dePtr += 1
                if dePtr < len(deadEnds):
                    leftWall = height[deadEnds[dePtr]]
                continue
            
            if h > leftWall:
                leftWall = h
            else:
                total += leftWall - h
        
        return total