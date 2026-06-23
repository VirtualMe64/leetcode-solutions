# Problem: https://leetcode.com/problems/3sum-closest
# Runtime: 1978 ms

from bisect import bisect_left

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        # print(nums)

        best = None
        bestDiff = None

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                curr = nums[i] + nums[j]
                diff = target - curr

                idx = bisect_left(nums[j + 1:], diff)

                if j + idx + 1 < len(nums):
                    option1 = nums[j + 1 + idx]
                    result1 = curr + option1
                    diff1 = abs(target - result1)

                    if bestDiff is None or diff1 < bestDiff:
                        best = result1
                        bestDiff = diff1

                if idx > 0:
                    option2 = nums[j + idx]
                    result2 = curr + option2
                    diff2 = abs(target - result2)
                
                    if bestDiff is None or diff2 < bestDiff:
                        best = result2
                        bestDiff = diff2
        
        return best