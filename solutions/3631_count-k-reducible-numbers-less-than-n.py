# Problem: https://leetcode.com/problems/count-k-reducible-numbers-less-than-n
# Runtime: 2868 ms

import math

class Solution:
    def isKReducible(self, n, k):
        if n == 1:
            return True
        for i in range(k):
            n = n.bit_count()
            if n == 1:
                return True
        return False
    
    def waysToPlace(self, s, o):
        MOD = (10 ** 9) + 7
    
        # calculate ways to place o 1s s.t the result is less than s
        # idea is scan and solve how many ways when we place all 1s to the left of index
        rem = o
        total = 0
        for i, c in enumerate(s):
            if c == '1':
                if rem == 0:
                    return total + 1
                # (len(s) - i - 1) spots to place (rem ones)
                # (len(s) - i - 1) choose rem
                total += math.comb(len(s) - i - 1, rem) % MOD
                rem -= 1
        return total
    
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        # after one iteration, we are at max 800 -- so manually solve that
        # then question is, how many numbers less than n with correct number of
        # it's giving stars and bars but < is annoying
        
        MOD = (10 ** 9) + 7
        
        if k == 5:
            # every number between 1 and 800 is 4-reducible, so we could set every bit if we want
            # therefore answer is n - 1
            return (int(s, 2) - 1) % MOD
        
        total = 0
        
        for i in range(1, len(s)):
            if self.isKReducible(i, k - 1):
                total += self.waysToPlace(s, i) % MOD
                total = total % MOD
        
        return total