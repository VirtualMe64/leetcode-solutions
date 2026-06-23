# Problem: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string
# Runtime: 0 ms

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = (2 ** n) - 1

        if n == 1: return "0"

        if k <= length // 2:
            return self.findKthBit(n - 1, k)
        elif k == (length // 2) + 1:
            return "1"
        else:
            # [length // 2][1][length // 2]
            baseIndex = k - (length // 2) - 1
            index = (length // 2 ) - baseIndex + 1
            return "1" if self.findKthBit(n - 1, index) == "0" else "0"