# Problem: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i
# Runtime: 19 ms

from bisect import bisect_left

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        occurences = {}
        out = []

        for i in range(len(nums)):
            occurences[nums[i]] = occurences.get(nums[i], 0) + 1
            if i - k >= 0:
                occurences[nums[i - k]] -= 1
            if i - k >= -1:
                byFreq = list(occurences.items())
                byFreq.sort(key = lambda x : (x[1], x[0]), reverse=True)
            
                out.append(sum([kv[0] * kv[1] for kv in byFreq[:x]]))

        return out