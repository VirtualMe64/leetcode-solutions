# Problem: https://leetcode.com/problems/reducing-dishes
# Runtime: 94 ms

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # simple idea: iterate over all possible lengths
        # optimal solution for given length is greedy
        # sort satisfaction list before to make computation easy
        # will be O(n^2) after sorting (so O(n^2)) overall
        satisfaction.sort(reverse = True)

        best = 0
        for l in range(1, len(satisfaction) + 1):
            curr = l
            idx = 0
            total = 0
            while curr > 0:
                total += curr * satisfaction[idx]
                curr -= 1
                idx += 1
            best = max(total, best)
        return best