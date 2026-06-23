# Problem: https://leetcode.com/problems/minimum-cost-to-convert-string-i
# Runtime: 259 ms

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # use floyd-warshall to get shortest all to all for letters
        # costs[i][j] = cost to go FROM i TO j
        swapCosts = [[float('inf') for i in range(26)] for j in range(26)]
        
        allChars = set()

        for i in range(len(original)):
            start = ord(original[i]) - ord('a')
            end = ord(changed[i]) - ord('a')
            weight = cost[i]

            if weight < swapCosts[start][end]:
                swapCosts[start][end] = weight

            allChars.add(start)
            allChars.add(end)

        allChars = list(allChars)

        for c in allChars:
            swapCosts[c][c] = 0

        for k in allChars:
            for i in allChars:
                for j in allChars:
                    if swapCosts[i][k] + swapCosts[k][j] < swapCosts[i][j]:
                        swapCosts[i][j] = swapCosts[i][k] + swapCosts[k][j]
        
        total = 0

        for s, d in zip(source, target):
            total += swapCosts[ord(s) - ord('a')][ord(d) - ord('a')]

        return total if not math.isinf(total) else -1