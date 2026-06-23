# Problem: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three
# Runtime: 0 ms

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            if n % 3 != 0:
                total += 1
        return total