# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
# Runtime: 0 ms

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] < nums[-1]: # right of min
                right = mid
            else:
                left = mid

        return nums[left]