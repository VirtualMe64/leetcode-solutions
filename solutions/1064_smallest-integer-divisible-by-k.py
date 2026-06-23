# Problem: https://leetcode.com/problems/smallest-integer-divisible-by-k
# Runtime: 3 ms

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 in [0, 2, 4, 5, 6, 8]:
            return -1

        remMap = {}
        curr = 0
        for i in range(10):
            remMap[(1 - curr) % 10] = k * i
            curr += (k % 10)

        curr = k
        place = 0
        while True:
            place += 1
            curr += remMap[curr % 10]
            curr //= 10

            if curr == 0:
                return place