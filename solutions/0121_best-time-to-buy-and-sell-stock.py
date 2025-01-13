# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Runtime: 740 ms

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bestProfit = 0
        minPrice = 10001
        for p in prices:
            minPrice = min(p, minPrice)
            profit = p - minPrice
            if profit > bestProfit:
                bestProfit = profit
        return bestProfit