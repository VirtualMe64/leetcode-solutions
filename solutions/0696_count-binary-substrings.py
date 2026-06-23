# Problem: https://leetcode.com/problems/count-binary-substrings
# Runtime: 34 ms

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevCount = 0
        currCount = 0
        currType = 0
        total = 0

        for c in s:
            if c != currType:
                total += min(prevCount, currCount)
                prevCount = currCount
                currCount = 0
                currType = c
        
            currCount += 1
        
        total += min(prevCount, currCount)

        return total