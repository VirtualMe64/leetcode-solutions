# Problem: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays
# Runtime: 3 ms

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        out = []
        n = 0

        for i in range(len(A)):
            if A[i] in seen: n += 1
            seen.add(A[i])
            if B[i] in seen: n += 1
            seen.add(B[i])

            out.append(n)

        return out