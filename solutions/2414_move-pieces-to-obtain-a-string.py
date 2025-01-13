# Problem: https://leetcode.com/problems/move-pieces-to-obtain-a-string
# Runtime: 159 ms

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        requirements = {'L': 0, 'R': 0, '_': 0}
        
        for sChar, tChar in zip(start, target):
            # '_' is basically filler
            if sChar == '_':
                requirements['_'] -= 1
            if tChar == '_':
                requirements['_'] += 1

            # 'R' must be available when in target, since future ones cant help
            if sChar == 'R':
                if requirements['L'] > 0: # future Ls are blocked, requirement cant be met
                    return False
                requirements['R'] -= 1
            if tChar == 'R':
                if requirements['R'] >= 0:
                    return False
                requirements['R'] += 1
            
            # 'L' can never be below 0, since it will never be filled
            if tChar == 'L':
                if requirements['R'] < 0:
                    return False
                requirements['L'] += 1
            if sChar == 'L':
                if requirements['L'] <= 0: # L is never needed
                    return False
                requirements['L'] -= 1

        return requirements['L'] == 0 and requirements['R'] == 0 and requirements['_'] == 0