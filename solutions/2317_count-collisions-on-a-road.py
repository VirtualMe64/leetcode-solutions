# Problem: https://leetcode.com/problems/count-collisions-on-a-road
# Runtime: 107 ms

class Solution:
    def countCollisions(self, directions: str) -> int:
        movingCnt = 0
        stationaryCnt = 0
        collisions = 0

        for d in directions:
            if d == 'S':
                if movingCnt > 0:
                    collisions += movingCnt
                movingCnt = 0
                stationaryCnt = 1
            elif d == 'R':
                stationaryCnt = 0
                movingCnt += 1
            elif d == 'L':
                if movingCnt > 0:
                    collisions += 2 + (movingCnt - 1)
                    movingCnt = 0
                    stationaryCnt = 1
                elif stationaryCnt > 0:
                    collisions += 1
                    movingCnt = 0
                    stationaryCnt = 1
        
        return collisions