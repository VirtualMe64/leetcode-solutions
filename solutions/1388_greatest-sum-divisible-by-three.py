# Problem: https://leetcode.com/problems/greatest-sum-divisible-by-three
# Runtime: 106 ms

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, None, None] # max sum so far with value % 3 = idx

        for n in nums:
            par = n % 3
            newDp = []
            for i in range(3):
                idx = (i - par) % 3

                if dp[idx] is None:
                    newDp.append(dp[i])
                    continue
                
                option = n + dp[idx]
                newDp.append(max(dp[i], option) if dp[i] is not None else option)
            dp = newDp

        return dp[0]