# Problem: https://leetcode.com/problems/maximum-total-damage-with-spell-casting
# Runtime: 621 ms

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = {}

        for p in power:
            counts[p] = counts.get(p, 0) + 1
        
        sortedPowers = sorted(counts.items(), key = lambda x : x[0])

        dp = [0 for i in range(len(sortedPowers))]

        for i in range(len(sortedPowers)):
            val, cnt = sortedPowers[i]
            damage = cnt * val

            prev1Match = i > 0 and sortedPowers[i - 1][0] == val - 1
            prev2Match = (i > 0 and sortedPowers[i - 1][0] == val - 2) or (i > 1 and sortedPowers[i - 2][0] == val - 2)

            # print(prev1Match, prev2Match)

            offset = -1
            options = []
            if prev1Match:
                options.append(dp[i + offset])
                offset -= 1
            if prev2Match:
                options.append(dp[i + offset])
                offset -= 1
            
            prevVal = 0 if i + offset < 0 else dp[i + offset]
            options.append(prevVal + damage)
            dp[i] = max(options)
        
        return dp[-1]