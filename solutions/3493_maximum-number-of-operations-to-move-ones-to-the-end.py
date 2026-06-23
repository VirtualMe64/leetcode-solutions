# Problem: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end
# Runtime: 64 ms

class Solution:
    def maxOperations(self, s: str) -> int:
        total = 0
        prev1s = 0
        
        for i in range(len(s) - 1):
            if s[i] != '1':
                continue
            
            prev1s += 1
            if s[i + 1] != '1':
                total += prev1s
        
        return total