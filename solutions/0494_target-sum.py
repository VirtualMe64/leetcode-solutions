# Problem: https://leetcode.com/problems/target-sum
# Runtime: 91 ms

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = {0: 1}

        for n in nums:
            newWays = {}
            for w, cnt in ways.items():
                newWays[w + n] = newWays.get(w + n, 0) + cnt
                newWays[w - n] = newWays.get(w - n, 0) + cnt
            ways = newWays

        return ways.get(target, 0)