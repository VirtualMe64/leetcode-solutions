# Problem: https://leetcode.com/problems/partition-equal-subset-sum
# Runtime: 250 ms

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # idea 1: all we need to do if find if subset sums to sum(nums) / 2
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2

        possibleSums = set([0])
        for n in nums:
            newSums = possibleSums.copy()
            for currSum in possibleSums:
                option = currSum + n
                if option > target:
                    continue
                if option == target:
                    return True
                newSums.add(option)
            possibleSums = newSums
        return False