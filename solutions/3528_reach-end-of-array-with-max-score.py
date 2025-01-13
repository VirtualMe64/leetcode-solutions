# Problem: https://leetcode.com/problems/reach-end-of-array-with-max-score
# Runtime: 1142 ms

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        score = 0
        currNum = nums[0]
        for num in nums[1::]:
            score += currNum
            if num > currNum:
                currNum = num
        return score