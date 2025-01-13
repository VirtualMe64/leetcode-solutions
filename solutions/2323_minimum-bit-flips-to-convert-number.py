# Problem: https://leetcode.com/problems/minimum-bit-flips-to-convert-number
# Runtime: 25 ms

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
    
        while start > 0 or goal > 0:
            startLSB = start & 1
            targetLSB = goal & 1
            
            if startLSB != targetLSB:
                flips += 1
        
            start = start >> 1 if start > 0 else 0
            goal = goal >> 1 if goal > 0 else 0
        
        return flips