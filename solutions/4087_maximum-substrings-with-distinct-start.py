# Problem: https://leetcode.com/problems/maximum-substrings-with-distinct-start
# Runtime: 15 ms

class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))