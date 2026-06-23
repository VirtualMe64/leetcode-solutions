# Problem: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i
# Runtime: 23 ms

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(c) for c in s]

        while len(nums) > 2:
            newNums = []

            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i + 1]) % 10)
            
            nums = newNums
        
        return nums[0] == nums[1]