# Problem: https://leetcode.com/problems/longest-balanced-subarray-i
# Runtime: 1323 ms

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        longest = 0

        for i in range(len(nums)):
            evenSet = set()
            oddSet = set()

            for j in range(i, len(nums)):
                n = nums[j]
                if n % 2 == 0:
                    evenSet.add(n)
                else:
                    oddSet.add(n)
                if len(evenSet) == len(oddSet):
                    longest = max(longest, j - i + 1)
        
        return longest