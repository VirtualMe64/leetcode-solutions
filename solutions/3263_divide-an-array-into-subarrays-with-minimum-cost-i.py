# Problem: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i
# Runtime: 1 ms

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min2 = []

        for n in nums[1:]:
            if len(min2) < 2:
                min2.append(n)
                continue
            
            maxVal = max(min2)
            if n < maxVal:
                min2.remove(maxVal)
                min2.append(n)
        
        return sum(min2) + nums[0]