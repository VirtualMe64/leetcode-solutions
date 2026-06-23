# Problem: https://leetcode.com/problems/longest-valid-parentheses
# Runtime: 11 ms

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        lastValid = None
        longest = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i if lastValid is None else lastValid)
                lastValid = None
            else:
                if len(stack) == 0:
                    lastValid = None
                    continue
                
                corresponding = stack.pop(-1)
                lastValid = corresponding
                longest = max(longest, i - lastValid + 1)
    
        return longest