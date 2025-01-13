# Problem: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i
# Runtime: 651 ms

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # longest subsequence with alternating parity or same parity
        alternating = 1
        curr = 1
        last = nums[0] % 2
        
        oddCount = int(last)
        evenCount = 1 - oddCount
        
        for num in nums[1:]:
            if num % 2 != last:
                curr += 1
                alternating = max(curr, alternating)
                last = num % 2
            oddCount += int(num % 2)
            evenCount += 1 - int(num % 2)
    

        return max(oddCount, evenCount, alternating)