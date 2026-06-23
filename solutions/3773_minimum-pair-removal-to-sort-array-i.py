# Problem: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i
# Runtime: 15 ms

import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def isSorted(nums):
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    return False
            
            return True

        count = 0
        while not isSorted(nums):
            count += 1

            minSumIdx = 0
            minSum = nums[0] + nums[1]

            for i in range(1, len(nums) - 1):
                if nums[i] + nums[i + 1] < minSum:
                    minSum = nums[i] + nums[i + 1]
                    minSumIdx = i
            
            newNums = []
            for i in range(len(nums)):
                if i == minSumIdx + 1:
                    continue
                elif i == minSumIdx:
                    newNums.append(minSum)
                else:
                    newNums.append(nums[i])

            # print(nums, newNums)

            nums = newNums

        return count