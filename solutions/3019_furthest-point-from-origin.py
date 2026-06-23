# Problem: https://leetcode.com/problems/furthest-point-from-origin
# Runtime: 0 ms

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = moves.count('L')
        r_count = moves.count('R')
        wild_count = moves.count('_')

        return abs(l_count - r_count) + wild_count