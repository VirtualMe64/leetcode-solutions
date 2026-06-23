# Problem: https://leetcode.com/problems/minimum-moves-to-make-array-complementary
# Runtime: 199 ms

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        costs = [0 for i in range((2 * limit) + 2)]

        for i in range(n // 2):
            left = nums[i]
            right = nums[n - i - 1]

            cost0 = left + right # costs 0 since that's already the sum
            cost1_left = min(left, right) + 1
            cost1_right = max(left, right) + limit
            
            costs[0] += 2
            costs[cost1_left - 1] -= 1
            costs[cost0 - 1] -= 1
            costs[cost0] += 1
            costs[cost1_right] += 1

        best = n
        total = 0
        for c in costs:
            total += c
            best = min(total, best)
        return best