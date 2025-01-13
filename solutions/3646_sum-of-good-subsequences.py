# Problem: https://leetcode.com/problems/sum-of-good-subsequences
# Runtime: 1257 ms

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        # sum based on starting num
        # go in reverse storing count + sum
        # to be efficient, use dict and check num + 1 and num - 1
        
        MOD = (10 ** 9) + 7
        
        # num: (count, sum)
        dp = {}
        total = 0
        
        for i in range(0, len(nums)):
            idx = len(nums) - i - 1
            
            count = 1
            seqSum = nums[idx]
            
            if nums[idx] + 1 in dp:
                otherCount, otherSum = dp[nums[idx] + 1]
                count += otherCount
                seqSum += (otherCount * nums[idx]) + otherSum
                seqSum %= MOD
            if nums[idx] - 1 in dp:
                otherCount, otherSum = dp[nums[idx] - 1]
                count += otherCount
                seqSum += (otherCount * nums[idx]) + otherSum
                seqSum %= MOD
            
            total += seqSum
            total %= MOD
            oldCount, oldSum = dp.get(nums[idx], (0, 0))
            dp[nums[idx]] = (count + oldCount, (seqSum + oldSum) % MOD)
        
        return total
        