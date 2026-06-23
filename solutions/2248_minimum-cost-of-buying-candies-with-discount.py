# Problem: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount
# Runtime: 0 ms

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for i, c in enumerate(cost):
            if i % 3 != 2:
                total += c
        return total