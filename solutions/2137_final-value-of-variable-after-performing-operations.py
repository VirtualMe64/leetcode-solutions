# Problem: https://leetcode.com/problems/final-value-of-variable-after-performing-operations
# Runtime: 0 ms

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        out = 0

        for o in operations:
            if o[0] == '+' or o[-1] == '+':
                out += 1
            else:
                out -= 1
        
        return out