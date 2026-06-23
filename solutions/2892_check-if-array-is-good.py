# Problem: https://leetcode.com/problems/check-if-array-is-good
# Runtime: 0 ms

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1

        count = {}

        for num in nums:
            if num > n:
                # base n array cannot contain values > n
                return False
            count[num] = count.get(num, 0) + 1
            if count[num] > 1 + (1 if num == n else 0):
                # base n array can only contain 1 of values less than n, and 2 of n
                return False
        
        return True