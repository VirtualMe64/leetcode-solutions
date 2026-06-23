# Problem: https://leetcode.com/problems/maximum-building-height
# Runtime: 271 ms

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort(key = lambda x : x[0])
        restrictions.insert(0, [1, 0])

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        for i in range(len(restrictions)):
            # building at position i cannot have height > i - 1
            restrictions[i][1] = min(restrictions[i][1], restrictions[i][0] - 1)
        
        def ripple():
            for i in range(len(restrictions) - 1):
                i1 = restrictions[i][0]
                r1 = restrictions[i][1]
                i2 = restrictions[i + 1][0]
                r2 = restrictions[i + 1][1]

                # a building x spots later cannot exceed height h + x
                restrictions[i + 1][1] = min(r2, r1 + abs(i2 - i1))

        # ripple the restrictions forward and backwards
        ripple()
        restrictions.reverse()
        ripple()
        restrictions.reverse()

        maxHeight = 0

        for i in range(len(restrictions) - 1):
            # for a given gap every 2 excess can get us 1 extra height
            i1 = restrictions[i][0]
            r1 = restrictions[i][1]
            i2 = restrictions[i + 1][0]
            r2 = restrictions[i + 1][1]

            iDiff = abs(i2 - i1)
            rDiff = abs(r2 - r1)
            rUpper = max(r1, r2)

            segMaxHeight = rUpper + ((iDiff - rDiff) // 2)

            # print(restrictions[i], restrictions[i + 1], segMaxHeight)

            maxHeight = max(maxHeight, segMaxHeight)
        
        return maxHeight