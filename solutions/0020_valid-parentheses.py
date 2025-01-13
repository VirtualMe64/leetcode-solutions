# Problem: https://leetcode.com/problems/valid-parentheses
# Runtime: 14 ms

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                queue.append(c)
            if c == ')':
                if len(queue) == 0:
                    return False
                top = queue.pop()
                if top != '(':
                    return False
            if c == ']':
                if len(queue) == 0:
                    return False
                top = queue.pop()
                if top != '[':
                    return False
            if c == '}':
                if len(queue) == 0:
                    return False
                top = queue.pop()
                if top != '{':
                    return False
        return len(queue) == 0