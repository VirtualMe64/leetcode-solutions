# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# Runtime: 0 ms

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    total = 0
    lastPrice = prices[0]
    prices.each do |p|
        total += p - lastPrice if p > lastPrice
        lastPrice = p
    end
    return total
end