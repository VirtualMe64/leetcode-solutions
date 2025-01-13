# Problem: https://leetcode.com/problems/maximum-subarray
# Runtime: 529 ms

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]

        for i, n in enumerate(nums[1:]):
            curr = max(n, curr + n)
            if curr > best:
                best = curr

        return best