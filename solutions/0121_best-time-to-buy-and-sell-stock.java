// Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution {
    public int maxProfit(int[] prices) {
        int cheapest = prices[0];
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            int val = prices[i];

            if (val < cheapest) {
                cheapest = val;
            }
            if (val - cheapest > maxProfit) {
                maxProfit = val - cheapest;
            }
        }
        
        return maxProfit;
    }
}