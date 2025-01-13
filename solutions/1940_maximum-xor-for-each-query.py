# Problem: https://leetcode.com/problems/maximum-xor-for-each-query
# Runtime: 35 ms

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (2 ** maximumBit) - 1
        out = []

        curr = 0
        for num in nums:
            curr = curr ^ num
            out.append((~curr) & mask)

        return out[::-1]