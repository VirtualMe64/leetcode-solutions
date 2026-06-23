# Problem: https://leetcode.com/problems/count-subarrays-with-score-less-than-k
# Runtime: 151 ms

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # naive: n^2 sub arrays, running sum array for O(1) eval
        # better: two pointer approach
        # intution: maintain widest possible range
        # if a certain size range is valid, every smaller one contained is valid too
        # count by ending ptr idx
        # only move right, so O(n)
        ptr1 = 0
        ptr2 = 0
        currVal = nums[0]
        cnt = 0
        while ptr2 < len(nums):
            subLen = ptr2 - ptr1 + 1 # length of current subarray
            valid = currVal * subLen < k
            if valid:
                cnt += subLen # each smaller array ending in ptr2 is valid
                ptr2 += 1
                if ptr2 < len(nums):
                    currVal += nums[ptr2] # add new value in subarray
            else: # invalid!
                if ptr1 == ptr2: # shift both
                    ptr2 += 1
                    if ptr2 < len(nums):
                        currVal += nums[ptr2] # add new value in subarry
                ptr1 += 1
                currVal -= nums[ptr1 - 1] # subtract removed value from subarray

        return cnt