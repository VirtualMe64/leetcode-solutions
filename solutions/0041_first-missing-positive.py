# Problem: https://leetcode.com/problems/first-missing-positive
# Runtime: 59 ms

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # naive: cocktail shaker
        
        limit = len(nums)
        i = 0
        while i < len(nums):
            n = nums[i]
            if n <= limit and n > 0:
                if nums[n - 1] != n:
                    nums[i] = nums[n - 1]
                    nums[n - 1] = n
                    if n - 1 > i:
                        i -= 1
            i += 1

        # print(nums)

        for i, n in enumerate(nums):
            if i + 1 != n:
                return i + 1
        return limit + 1