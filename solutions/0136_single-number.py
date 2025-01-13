# Problem: https://leetcode.com/problems/single-number
# Runtime: 784 ms

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.append(num)
        return seen[0]