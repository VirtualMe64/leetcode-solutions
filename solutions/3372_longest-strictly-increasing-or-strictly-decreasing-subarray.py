# Problem: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray
# Runtime: 4 ms

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1
        curr = 1
        incr = True
        prev = nums[0]

        for n in nums[1:]:
            if n > prev:
                if incr:
                    curr += 1
                else:
                    incr = True
                    curr = 2
            elif n < prev:
                if incr:
                    incr = False
                    curr = 2
                else:
                    curr += 1
            else:
                curr = 1
            longest = max(longest, curr)
            prev = n

        return longest