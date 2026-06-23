# Problem: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero
# Runtime: 0 ms

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # 2^k (1000... with k zeroes)
        # 100.....1 after 1 op
        # 100....11 after 2 ops
        # 100....10 after 3 ops
        # 100...101 after 4 ops
        # 100...110 after 5 ops
        # notice, after n ops, the binary repr of n is on the right
        # thus, 
        # 010...000 after 2 ^ (k - 1)
        # now 2^(k - 1) -- recurses!
        # 2^(k - 1) + 2^(k - 2) + ... = 2^k - 1 ops
        # for remaining bits, have to figure out which iteration this is
        # 000 -> 001 -> 011 -> 010 -> 110 -> 111 -> 101 -> 100 -> 000
        # this is grey code!
        # actually the whole thing is just inverse grey code

        # https://www.johndcook.com/blog/2020/09/08/inverse-gray-code/

        x = n
        e = 1
        while x:
            x = n >> e
            e *= 2
            n = n ^ x
        return n