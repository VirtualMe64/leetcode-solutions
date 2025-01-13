# Problem: https://leetcode.com/problems/search-insert-position
# Runtime: 47 ms

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Given: nums: sorted arr distinct int ; target
        # want: index ; in O(logn)

        low = 0
        high = len(nums)

        while low < high:
            curr = (low + high - 1) // 2
            if nums[curr] == target:
                return curr
            if nums[curr] > target:
                high = curr
            if nums[curr] < target:
                low = curr + 1
        return low