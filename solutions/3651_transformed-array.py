# Problem: https://leetcode.com/problems/transformed-array
# Runtime: 64 ms

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        out = []

        for i in range(len(nums)):
            newIdx = (i + nums[i]) % len(nums)
            out.append(nums[newIdx])
        
        return out