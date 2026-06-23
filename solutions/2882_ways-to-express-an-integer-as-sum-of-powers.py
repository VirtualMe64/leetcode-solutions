# Problem: https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers
# Runtime: 1026 ms

MODULO = (10 ** 9) + 7

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # 1 -> 1
        # 2 -> 1
        # 3 -> 2
        # 4 -> 2
        # 5 -> 3
        # 6 -> 4
        # 7 -> 5

        options = []
        curr = 1
        while curr ** x <= n:
            options.append(curr ** x)
            curr += 1
        
        # dp[i][j] = number of ways to make (j + 1) using only options >= options[i]
        dp = []
        totals = []

        for i in range(n):
            newRow = [0]
            runningSum = 0
            for j, option in enumerate(options):
                target = i + 1
                if option > target:
                    runningSum += 0
                elif option == target:
                    runningSum += 1
                else:
                    rem = target - option
                    runningSum += totals[rem - 1] - dp[rem - 1][j + 1]
                newRow.append(runningSum % MODULO)
            dp.append(newRow)
            totals.append(runningSum % MODULO)

        return totals[-1] % MODULO