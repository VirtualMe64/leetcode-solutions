# Problem: https://leetcode.com/problems/maximum-multiplication-score
# Runtime: 1597 ms

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        # dp[i] = best score with first i elements of b (iterative updates for each elem of a)
        dp = []
        best = None
        for num in b:
            option = num * a[0]
            best = option if best == None else max(best, option)
            dp.append(best)

        for a_idx in range(1, 4):
            new_dp = [x for x in dp]
            new_dp[a_idx] = new_dp[a_idx - 1] + (b[a_idx] * a[a_idx])
            for i, num in enumerate(b[a_idx + 1:]):
                dp_idx = i + a_idx + 1
                choice = max(new_dp[dp_idx - 1], dp[dp_idx - 1] + (a[a_idx] * b[dp_idx]))
                new_dp[dp_idx] = choice
            dp = new_dp
        
        return dp[-1]