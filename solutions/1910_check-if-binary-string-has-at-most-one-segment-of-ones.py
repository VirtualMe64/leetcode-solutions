# Problem: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones
# Runtime: 0 ms

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return not '01' in s