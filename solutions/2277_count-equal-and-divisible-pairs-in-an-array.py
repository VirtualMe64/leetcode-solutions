# Problem: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array
# Runtime: 23 ms

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    total += 1
        return total