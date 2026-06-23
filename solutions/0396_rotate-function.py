# Problem: https://leetcode.com/problems/rotate-function
# Runtime: 133 ms

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # for simplicity, we say rotations are counterclockwise
        # going from k to k - 1 decrements coefficient of most terms
        # (k - 1)th term goes from coefficient of 0 to (n - 1)
        # observation: f(k) = f(k - 1) - sum(nums) + (n  * nums[k - 1])
        n = len(nums)
        total = sum(nums)
        curr = sum([i * nums[i] for i in range(n)]) # start with f(0)
        best = curr

        for k in range(1, n):
            curr = curr - total + (n * nums[k - 1])
            best = max(best, curr)
        
        return best