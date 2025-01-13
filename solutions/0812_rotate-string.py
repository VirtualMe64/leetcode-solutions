# Problem: https://leetcode.com/problems/rotate-string
# Runtime: 0 ms

class Solution:
    def checkRotation(self, s, goal, rotation):
        ptr2 = rotation

        for ptr1 in range(len(s)):
            if s[ptr1] != goal[(ptr2 + ptr1) % len(goal)]:
                return False
        
        return True

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for rot in range(len(s)):
            if self.checkRotation(s, goal, rot):
                return True
        
        return False