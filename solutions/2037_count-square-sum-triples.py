# Problem: https://leetcode.com/problems/count-square-sum-triples
# Runtime: 102 ms

import math

class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        n_sq = n ** 2
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                sq = (a ** 2 + b ** 2)
                if sq > n_sq:
                    continue
                sqrt = math.sqrt(sq)
                if sqrt.is_integer():
                    cnt += 2
        
        return cnt