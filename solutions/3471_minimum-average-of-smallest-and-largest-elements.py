# Problem: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements
# Runtime: 45 ms

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        best = None
        while len(nums) > 0:
            lowest = nums.pop(0)
            highest = nums.pop()
            
            best = min(best, lowest + highest) if best else lowest + highest
        
        return best / 2