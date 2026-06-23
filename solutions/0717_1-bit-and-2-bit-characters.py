# Problem: https://leetcode.com/problems/1-bit-and-2-bit-characters
# Runtime: 0 ms

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1: return False
            
        prev1Count = 0

        for i in range(len(bits) - 1):
            if bits[-(i + 2)] == 0: break
            prev1Count += 1

        
        return prev1Count % 2 == 0