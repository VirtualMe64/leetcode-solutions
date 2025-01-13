# Problem: https://leetcode.com/problems/remove-invalid-parentheses
# Runtime: 66 ms

from itertools import combinations

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if ')' not in s or '(' not in s:
            return [s.replace('(', '').replace(')', '')]

        # step 1: remove all trailing and starting incorrect parenthese
        newStr = ""
        firstOpenIndex = s.index('(')
        lastClosedIndex = len(s) - s[::-1].index(')') - 1
        for i, char in enumerate(s):
            if i < firstOpenIndex and char == ')':
                continue
            if i > lastClosedIndex and char == '(':
                continue
            newStr += char
        
        out = []
        visited = set([newStr])
        frontier = [(newStr, 0)]
        targetDepth = None
        while len(frontier) > 0:
            curr = frontier.pop(0)
            if targetDepth != None and curr[1] != targetDepth:
                continue
            if self.isValid(curr[0]):
                out.append(curr[0])
                targetDepth = curr[1]
            for neighbor in self.getNeighbors(curr[0]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    frontier.append((neighbor, curr[1] + 1))
        return out

    def isValid(self, s : str):
        counter = 0
        for char in s:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
                if counter < 0:
                    return False
        return counter == 0
    
    def getNeighbors(self, s : str):
        out = set()
        for i, char in enumerate(s):
            if char == '(' or char == ')':
                out.add(s[0:i] + s[i + 1:])
        return out