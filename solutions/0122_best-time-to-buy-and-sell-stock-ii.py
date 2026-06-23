# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# Runtime: 2 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1)])