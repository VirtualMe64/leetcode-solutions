# Problem: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away
# Runtime: 5 ms

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last1 = -(k + 1)

        for i, n in enumerate(nums):
            if n == 1:
                if i - last1 <= k:
                    return False
                last1 = i
        
        return True