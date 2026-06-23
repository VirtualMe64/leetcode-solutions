# Problem: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i
# Runtime: 0 ms

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        byNum = {}

        for i, n in enumerate(nums):
            if n not in byNum:
                byNum[n] = []
            byNum[n].append(i)

        best = -1
        for arr in byNum.values():
            for i in range(len(arr) - 2):
                val = (arr[i + 2] - arr[i]) * 2
                if best == -1 or val < best:
                    best = val
        return best