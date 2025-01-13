# Problem: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and
# Runtime: 668 ms

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best = 0
        bestLength = 0
        curr = 0
        currLength = 0

        for num in nums:
            if num > curr:
                curr = num
                currLength = 1
            elif num & curr == curr:
                currLength += 1
            else:
                curr = num
                currLength = 1
            
            if curr > best:
                best = curr
                bestLength = currLength
            elif curr == best:
                bestLength = max(currLength, bestLength)

        return bestLength