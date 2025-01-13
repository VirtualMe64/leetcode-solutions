# Problem: https://leetcode.com/problems/k-divisible-elements-subarrays
# Runtime: 447 ms

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        totalDivisibleTable = [0] * len(nums)
        if nums[0] % p == 0:
            totalDivisibleTable[0] = 1
        
        # step 1: build table of entries <= i divisible by p
        for i, num in enumerate(nums[1:]):
            totalDivisibleTable[i + 1] = totalDivisibleTable[i] + (1 if num % p == 0 else 0)
        
        subarrays = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                firstVal = totalDivisibleTable[i - 1] if i > 0 else 0
                secondVal = totalDivisibleTable[j]
                if secondVal - firstVal <= k:
                    subarrays.add(tuple(nums[i : j + 1]))
        
        return len(subarrays)