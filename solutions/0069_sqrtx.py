# Problem: https://leetcode.com/problems/sqrtx
# Runtime: 4 ms

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left < right:
            mid = (right + left) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq > x:
                right = mid - 1
            else:
                left = mid + 1
        
        cand = left
        if cand * cand > x:
            return cand - 1
        else:
            return cand