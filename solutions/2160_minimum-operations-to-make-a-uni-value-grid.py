# Problem: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid
# Runtime: 113 ms

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        target = grid[0][0] % x

        nums = []
        for row in grid:
            for v in row:
                if v % x != target:
                    return -1
                nums.append(v // x)
        nums.sort()
        goal = nums[len(nums) // 2]

        out = 0
        for n in nums:
            out += abs(goal - n)
        return out