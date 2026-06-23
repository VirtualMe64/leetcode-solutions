# Problem: https://leetcode.com/problems/maximum-ice-cream-bars
# Runtime: 27 ms

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        counts = [0] * (max_cost + 1)
        for c in costs:
            counts[c] += 1
        
        out = 0
        for cost in range(max_cost + 1):
            c = counts[cost]
            if c == 0: continue

            mostPossible = coins // cost

            if mostPossible < c:
                out += mostPossible
                coins -= mostPossible * cost
                return out
            else:
                out += c
                coins -= c * cost

            if coins < cost:
                return out
        
        return out