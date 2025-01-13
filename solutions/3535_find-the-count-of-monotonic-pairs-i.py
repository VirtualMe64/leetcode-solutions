# Problem: https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i
# Runtime: 1812 ms

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        # simple case, one number nums[0] = i
        # solution is n + 1 (arr1[0] from 0 to n)

        # feels dp
        # dp[i][j]: solutions for the first j of nums, last number of arr2 is i
        # base cases:
        # dp[0][0] = 0 
        # dp[i][0] = 1 if i <= nums[0] else 0
        # recurrence:
        # intuition, dp[i_1][j] is sum of some values from dp[i_2][j - 1]
        #    condition 0: i_1 <= nums[j]
        #    condition 1: i_2 >= i_1 to keep arr1 non-increasing
        #    condition 2: nums[j] - i_1 > nums[j - 1] - i_2 to keep arr2 non-decreasing 
        #                 so i_2 > nums[j - 1] + i_1 - nums[j]
        # dp[i][j]: sum of previous where 

        # [2, 3, 2]
        # [1  3  3]
        # [1  2  1]
        # [1  1  0]
        # [0  0  0]
        VAL = ((10 ** 9) + 7)

        last = [1 if i <= nums[0] else 0 for i in range(max(nums) + 1)]
        new = []

        for j in range(1, len(nums)):
            for i in range(len(last)):
                if i > nums[j]:
                    new.append(0)
                    continue
                cond1 = i
                cond2 = nums[j - 1] + i - nums[j]

                total = 0
                for prev in range(max(cond1, cond2), len(last)):
                    total += last[prev]
                new.append(total % VAL)
            
            last = new
            new = []

        res = sum(last)
        return res % VAL