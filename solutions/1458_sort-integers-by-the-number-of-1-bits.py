# Problem: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits
# Runtime: 14 ms

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def numOnes(n):
            v = n
            cnt = 0
            while v > 0:
                if v % 2 == 1: cnt += 1
                v >>= 1
            return (cnt, n)
        return sorted(arr, key = numOnes)