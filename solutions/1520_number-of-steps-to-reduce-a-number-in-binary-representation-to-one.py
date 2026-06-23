# Problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
# Runtime: 0 ms

class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, base=2)
        steps = 0

        while num != 1:
            if num % 2 == 0: num >>= 1
            else: num += 1
            steps += 1
        
        return steps