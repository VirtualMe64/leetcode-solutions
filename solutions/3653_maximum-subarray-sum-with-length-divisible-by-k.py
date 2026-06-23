# Problem: https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k
# Runtime: 534 ms

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        dp = [(None, 0) for i in range(k)] # max from last chunk, running sum after

        best = None

        for i, n in enumerate(nums):
            prev = dp[(i - 1) % k]
            curr = dp[i % k]
            chunkSum = prev[1] - curr[1] + n
            chunkMax = max(0, 0 if curr[0] is None else curr[0]) + chunkSum
            if i >= k - 1:
                best = max(best, chunkMax) if best is not None else chunkMax

            dp[i % k] = (
                chunkMax if i >= k - 1 else None,
                prev[1] + n
            )

        return best