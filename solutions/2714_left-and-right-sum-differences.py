# Problem: https://leetcode.com/problems/left-and-right-sum-differences
# Runtime: 3 ms

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        tot = sum(nums)
        out = []

        for i in range(len(nums)):
            tot -= nums[i]
            if i > 0: tot -= nums[i - 1]
            out.append(abs(tot))
        
        return out