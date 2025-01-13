# Problem: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii
# Runtime: 1374 ms

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        increasingLengths = [0 for i in range(len(nums))]
        
        last = -1001
        length = 0
        for i, num in enumerate(nums):
            if num > last:
                length += 1
            else:
                length = 1
            last = num
            increasingLengths[i] = length
        
        k = 0
        
        for i in range(0, len(nums)):
            if i + k + 1>= len(nums):
                return k
            
            potential = k + 1
            while (i + potential < len(nums) and increasingLengths[i] >= potential and increasingLengths[i + potential] >= potential):
                k += 1
                potential += 1
        
        return k