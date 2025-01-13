# Problem: https://leetcode.com/problems/extra-characters-in-a-string
# Runtime: 161 ms

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        maxLength = max([len(w) for w in dictionary])
        wordSet = set(dictionary)

        # dp[i] stores min extra chars for the first i characters
        dp = [None for i in range(len(s) + 1)]
        dp[0] = 0
        
        for i in range(1, len(s) + 1):
            best = None
            for j in range(max(0, i - maxLength), i):
                option = (i - j) + dp[j]
                if s[j:i] in wordSet:
                    option = min(option, dp[j])
                best = min(best, option) if best is not None else option
            dp[i] = best
        
        return dp[-1]