# Problem: https://leetcode.com/problems/ones-and-zeroes
# Runtime: 2066 ms

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # idea 1: 3d dp across m, n, and first s strings
        # dp[s, m, n]
        dp = [[0 for k in range(n + 1)] for j in range(m + 1)]
        newDp = [[0 for k in range(n + 1)] for j in range(m + 1)]

        for s in range(len(strs)):
            num0 = strs[s].count('0')
            num1 = strs[s].count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    base = dp[j][k]
                
                    if num0 > j:
                        val = base
                    elif num1 > k:
                        val = base
                    else:
                        val = dp[j - num0][k - num1] + 1
                    
                    newDp[j][k] = max(base, val)

            dp = [[v for v in r] for r in newDp]

        return dp[-1][-1]