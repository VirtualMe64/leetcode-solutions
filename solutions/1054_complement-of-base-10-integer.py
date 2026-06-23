# Problem: https://leetcode.com/problems/complement-of-base-10-integer
# Runtime: 0 ms

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1

        p1 = 0
        i = 0

        # print(bin(n))

        while n > 0:
            p1 *= 2
            if n % 2 == 1:
                p1 += 1
            
            n >>= 1
            i += 1

        # print(bin(p1))

        p2 = 0
        for _ in range(i):
            p2 *= 2
            if p1 % 2 == 0:
                p2 += 1
            p1 >>= 1

        # print(bin(p2))
    
        return p2