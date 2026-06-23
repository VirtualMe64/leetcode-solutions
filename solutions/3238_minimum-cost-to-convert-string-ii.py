# Problem: https://leetcode.com/problems/minimum-cost-to-convert-string-ii
# Runtime: 6877 ms

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 1. use floyd-warshall to get shortest path from all substrs to each other
        allSubstrs = set()
        lengths = set([1])
        for i in range(len(original)):
            allSubstrs.add(original[i])
            allSubstrs.add(changed[i])
            lengths.add(len(original[i]))
            lengths.add(len(changed[i]))

        allSubstrs = list(allSubstrs)
        lengths = sorted(list(lengths))
        substrMap = {}
        for i, s in enumerate(allSubstrs):
            substrMap[s] = i

        # swapCosts[i][j] is cost to go FROM substr i TO substr j
        swapCosts = [[float('inf') for i in range(len(allSubstrs))] for j in range(len(allSubstrs))]

        for i in range(len(original)):
            start = substrMap[original[i]]
            end = substrMap[changed[i]]
            weight = cost[i]

            if weight < swapCosts[start][end]:
                swapCosts[start][end] = weight

        for i in range(len(allSubstrs)):
            swapCosts[i][i] = 0

        for k in range(len(allSubstrs)):
            for i in range(len(allSubstrs)):
                for j in range(len(allSubstrs)):
                    if swapCosts[i][k] + swapCosts[k][j] < swapCosts[i][j]:
                        swapCosts[i][j] = swapCosts[i][k] + swapCosts[k][j]
        
        # 2. use DP to find cheapest way to get to target
        conversionCosts = [0] # ith entry is minimum cost to convert source[:i]
        for i in range(len(source)):
            best = float('inf')
            for l in lengths:
                j = i - l + 1
                if j < 0:
                    break

                sourceStub = source[j:i + 1]
                targetStub = target[j:i + 1]

                if sourceStub == targetStub: # no swapping needed
                    best = min(best, conversionCosts[j])
                elif sourceStub in substrMap and targetStub in substrMap:
                    baseCost = swapCosts[substrMap[sourceStub]][substrMap[targetStub]]
                    totalCost = baseCost + conversionCosts[j]
                    best = min(best, totalCost)
            conversionCosts.append(best)

        return conversionCosts[-1] if not math.isinf(conversionCosts[-1]) else -1