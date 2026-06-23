# Problem: https://leetcode.com/problems/count-special-triplets
# Runtime: 380 ms

MOD = 10 ** 9 + 7

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # need: how may prior (n, n // 2) count
        # requires: how many prior (n, ) counts

        counts = {}
        twoCounts = {}
        total = 0

        for n in nums:
            if n % 2 == 0:
                total += twoCounts.get(n // 2, 0)
            twoCounts[n] = twoCounts.get(n, 0) + counts.get(n * 2, 0)
            counts[n] = counts.get(n, 0) + 1

        return total % MOD