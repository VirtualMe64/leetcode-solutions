# Problem: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end
# Runtime: 80 ms

class Solution:
    def maxOperations(self, s: str) -> int:
        # always do leftmost block, from right to left
        # chains of 1s are good since we get to move them one at a time 
        # can prob solve efficiently by scanning and keeping some type of counter
        
        total = 0
        blockSize = 0
        inBlock = False
        
        for c in s:
            if c == '1':
                blockSize += 1
                inBlock = True
            elif c == '0':
                if inBlock:
                    total += blockSize
                inBlock = False
        
        return total