# Problem: https://leetcode.com/problems/container-with-most-water
# Runtime: 528 ms

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptrRight = len(height) - 1
        ptrLeft = 0
        best = 0

        while ptrRight > ptrLeft:
            area = min(height[ptrLeft], height[ptrRight]) * (ptrRight - ptrLeft)
            best = max(best, area)
            if height[ptrRight] > height[ptrLeft]:
                ptrLeft += 1
            else:
                ptrRight -= 1
        return best