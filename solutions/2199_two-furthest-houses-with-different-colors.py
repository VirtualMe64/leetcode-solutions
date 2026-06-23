# Problem: https://leetcode.com/problems/two-furthest-houses-with-different-colors
# Runtime: 0 ms

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        def forwardTest(arr):
            best = 0
            for i in range(1, len(arr)):
                if arr[i] != arr[0]:
                    best = i
            return best

        return max(forwardTest(colors), forwardTest(colors[::-1]))