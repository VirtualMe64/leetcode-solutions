# Problem: https://leetcode.com/problems/count-number-of-trapezoids-i
# Runtime: 70 ms

MOD = 10 ** 9 + 7

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        byY = {}

        for p in points:
            byY[p[1]] = byY.get(p[1], 0) + 1
        
        total = 0
        prevSum = 0
        for v in byY.values():
            ways = (v * (v - 1)) // 2 # n points -> n choose 2 lines
            total = (total + (ways * prevSum)) % MOD
            prevSum = (prevSum + ways) % MOD

        return total