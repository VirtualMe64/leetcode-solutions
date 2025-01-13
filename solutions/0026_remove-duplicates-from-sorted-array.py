# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Runtime: 134 ms

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums.pop(index + 1)
            else:
                index += 1

        return len(nums)