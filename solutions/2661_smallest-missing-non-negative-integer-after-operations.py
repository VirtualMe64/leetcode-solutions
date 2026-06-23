# Problem: https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations
# Runtime: 99 ms

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        buckets = {}
        for num in nums:
            bucket = num % value

            buckets[bucket] = buckets.get(bucket, 0) + 1
        
        minVal = len(nums)

        for i in range(min(value, len(nums))):
            missing = (buckets.get(i, 0) * value) + i
            minVal = min(minVal, missing)
        
        return minVal