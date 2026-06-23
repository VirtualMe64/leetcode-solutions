# Problem: https://leetcode.com/problems/find-the-highest-altitude
# Runtime: 0 ms

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        best = 0
        curr = 0

        for g in gain:
            curr += g
            best = max(best, curr)
        
        return best