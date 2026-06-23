# Problem: https://leetcode.com/problems/coin-change
# Runtime: 331 ms

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]

        for i in range(1, amount + 1):
            best = -2
            for c in coins:
                option = i - c
                if option >= 0 and dp[option] != -1:
                    if best == -2 or dp[option] < best:
                        best = dp[option]
            dp.append(best + 1)

        return dp[-1]