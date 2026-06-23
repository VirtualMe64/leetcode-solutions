# Problem: https://leetcode.com/problems/trionic-array-i
# Runtime: 0 ms

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[1] <= nums[0]:
            return False

        seg = 0

        prev = nums[0]
        for n in nums[1:]:
            if n > prev:
                if seg == 1:
                    seg += 1
            elif n < prev:
                if seg == 0:
                    seg += 1
                elif seg == 2:
                    return False
            else:
                return False

            prev = n

        return seg == 2