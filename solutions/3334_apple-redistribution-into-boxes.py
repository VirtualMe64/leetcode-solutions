# Problem: https://leetcode.com/problems/apple-redistribution-into-boxes
# Runtime: 3 ms

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        idx = 0
        while total > 0:
            total -= capacity[idx]
            idx += 1
        return idx