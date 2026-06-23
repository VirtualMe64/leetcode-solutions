# Problem: https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k
# Runtime: 1005 ms

MOD = (10 ** 9) + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(k)]]
        dp[0][grid[0][0] % k] = 1

        for i in range(m + n - 2): # traverse down then right
            newDp = []
            vert = i + 1 < m
            idx = [i + 1, 0] if vert else [m - 1, i + 1 - m + 1]

            j = 0
            while idx[0] >= 0 and idx[1] < n:
                val = grid[idx[0]][idx[1]] % k
                leftIdx = j - 1 if vert else j
                rightIdx = j if vert else j + 1

                leftVals = dp[leftIdx] if 0 <= leftIdx < len(dp)  else None
                rightVals = dp[rightIdx] if 0 <= rightIdx < len(dp) else None
                
                counts = []

                for i in range(k):
                    base = 0
                    if leftVals is not None: base += leftVals[(i - val) % k]
                    if rightVals is not None: base += rightVals[(i - val) % k]
                    counts.append(base % MOD)

                newDp.append(counts)
                    
                j += 1
                idx[0] -= 1
                idx[1] += 1
        
            dp = newDp
        
        return dp[0][0]