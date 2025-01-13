# Problem: https://leetcode.com/problems/majority-element
# Runtime: 1 ms

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]