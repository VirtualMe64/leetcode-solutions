# Problem: https://leetcode.com/problems/successful-pairs-of-spells-and-potions
# Runtime: 223 ms

from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        out = []

        for s in spells:
            target = success / s
            idx = bisect_left(potions, target)

            out.append(len(potions) - idx)

        return out
