# Problem: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii
# Runtime: 3377 ms

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # k = 10
        # [30]
        
        
        nums = [n % k for n in nums]
        lastSeen = {}
        
        # dp table[i][d]: max length that includes index i in a cycle of sum s
        dp_table = [[0 for b in range(k)] for a in range(len(nums))]
        
        overallMax = 0
        
        for i, num in enumerate(nums):
            for target in range(k):
                # first option: add to the cycle
                needed = (target - num) % k
                option1 = -1 if needed not in lastSeen else dp_table[lastSeen[needed]][target] + 1
                
                # second option: take the last value
                option2 = -1 if num not in lastSeen else dp_table[lastSeen[num]][target]
                
                # final option: new size
                newVal = max(option1, option2, 1)
                dp_table[i][target] = newVal
                
                overallMax = max(overallMax, newVal)
            
            lastSeen[num] = i
        
        return overallMax