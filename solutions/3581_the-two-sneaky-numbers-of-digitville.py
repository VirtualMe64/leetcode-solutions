# Problem: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville
# Runtime: 47 ms

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        
        out = []
        
        for n in nums:
            if n in seen:
                out.append(n)
            seen.add(n)
        
        return out