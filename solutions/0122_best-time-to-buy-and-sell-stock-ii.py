# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# Runtime: 50 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lastPrice = prices[0]
        profit = 0

        for price in prices[1:]:
            if price > lastPrice:
                profit += price - lastPrice

            lastPrice = price
        
        return profit