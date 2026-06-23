# Problem: https://leetcode.com/problems/permutation-sequence
# Runtime: 3 ms

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return "1"

        factorials = [1]

        for i in range(2, n):
            factorials.append(factorials[-1] * i)

        out = []
        rem = [i for i in range(1, n + 1)]

        curr = k - 1
        while len(factorials) > 0:
            f = factorials.pop()
            idx = curr // f
            curr = curr % f

            out.append(rem.pop(idx))
        
        out.append(rem[0])

        return "".join([str(s) for s in out])