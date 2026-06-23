# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Runtime: 87 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = None
        bestSoFar = 0

        for p in prices:
            if minSoFar is None or p < minSoFar:
                minSoFar = p
            delta = p - minSoFar
            bestSoFar = max(delta, bestSoFar)
        
        return bestSoFar