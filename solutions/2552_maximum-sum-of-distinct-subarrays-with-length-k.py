# Problem: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
# Runtime: 138 ms

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = {}
        duplicates = set()
        currSum = 0

        best = 0
        for i, n in enumerate(nums):
            counts[n] = counts.get(n, 0) + 1
            if counts[n] == 2:
                duplicates.add(n)
            currSum += n
            if i == k - 1: # first time we get to max
                if len(duplicates) == 0:
                    best = currSum
            elif i >= k: # we are at max
                tail = nums[i - k]
                counts[tail] -= 1
                if counts[tail] == 1:
                    duplicates.remove(tail)
                currSum -= tail
                if len(duplicates) == 0:
                    best = max(best, currSum)
        
        return best