# Problem: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i
# Runtime: 69 ms

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        increasingLengths = [0 for i in range(len(nums))]

        last = -1001
        length = 0
        for i, n in enumerate(nums):
            if n > last:
                length += 1
            else:
                length = 1
            last = n
            increasingLengths[i] = length
     

        for left in range(k - 1, len(nums) - k):
            if increasingLengths[left] >= k and increasingLengths[left + k] >= k:
                return True

        return False