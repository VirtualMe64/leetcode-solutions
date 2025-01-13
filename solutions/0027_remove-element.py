# Problem: https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = 0
        for i in range(len(nums)):
            curr = nums[i - removed]
            if curr == val:
                nums.pop(i - removed)
                removed += 1
