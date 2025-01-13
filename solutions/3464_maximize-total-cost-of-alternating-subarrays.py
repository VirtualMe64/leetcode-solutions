# Problem: https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays
# Runtime: 433 ms

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        # [1, 1, -1200, -14, -10, -100000, 1]
        # max size of subarray may as well be 2
        # whenever we encounter positive number, may as well start new
        
        # total = 1, prev = 1, curr = 1
        # total = 2, prev = 1, curr = 1
        # total = 1200, prev = -1200, curr = -14
        # 
        
        total = nums[0]
        prev = abs(nums[0]) # pretend first is positive since we always take it
        prevGain = None
        
        for num in nums[1:]:
            if num >= 0:
                # if it's positive, we can always take it
                total += num
                prev = num
                continue
                
            if prev >= 0:
                # a negative after a positive is always free
                total -= num
                prev = num
                prevGain = -num
                continue
            
            # [1, -1, -2, -3]
            # in a negative following a negative, swapping benefits us -num - prevGain
            alt = -num - prevGain
            if alt > 0:
                total += alt
                total -= prevGain # since we already added so need to subtract twice
                prev = num    # if we see another negative after, we gotta decide again (this part might be wrong)
                prevGain = alt
            else:
                total += num
                prev = -num  # we can take a negative after this for free

        return total
            
            