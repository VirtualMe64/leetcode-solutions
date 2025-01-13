# Problem: https://leetcode.com/problems/maximum-product-subarray
# Runtime: 70 ms

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # edge case: one number
        if len(nums) == 1:
            return nums[0] 

        # dp idea: keep track of best subarray ending at i
        # track current best for negative AND positive
        firstPos = nums[0] >= 0
        lastPos = nums[0] if firstPos else 0
        lastNeg = 0 if firstPos else nums[0]

        res = nums[0]

        for i, num in enumerate(nums[1:]):
            # options: start new or add to prev
            newOption = num
            posOption = num * lastPos
            negOption = num * lastNeg

            lastPos = max(newOption, posOption, negOption)
            lastNeg = min(newOption, posOption, negOption)

            res = max(res, lastPos)

        return res