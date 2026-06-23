# Problem: https://leetcode.com/problems/separate-the-digits-in-an-array
# Runtime: 3 ms

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        out = []

        for n in nums:
            sep = []
            while n > 0:
                sep.append(n % 10)
                n //= 10
            out.extend(sep[::-1])
        
        return out