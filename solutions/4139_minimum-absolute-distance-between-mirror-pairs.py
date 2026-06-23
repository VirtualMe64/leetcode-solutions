# Problem: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs
# Runtime: 348 ms

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def getMirror(num):
            out = 0
            while num > 0:
                out *= 10
                out += num % 10
                num = num // 10
            return out

        latest = {}
        smallest = None
        for i, n in enumerate(nums):
            if n in latest:
                dist = i - latest[n]
                smallest = min(smallest, dist) if smallest is not None else dist
            latest[getMirror(n)] = i

        return smallest if smallest is not None else -1