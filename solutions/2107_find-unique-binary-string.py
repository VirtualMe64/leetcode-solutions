# Problem: https://leetcode.com/problems/find-unique-binary-string
# Runtime: 0 ms

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def format(n):
            base = bin(n)[2:]
            return ("0" * (len(nums) - len(base))) + base

        nums.sort()
        for i in range(len(nums)):
            if int(nums[i], base = 2) != i:
                return format(i)
        return format(len(nums))