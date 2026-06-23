# Problem: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i
# Runtime: 0 ms

import math

class Solution:
    def kthCharacter(self, k: int) -> str:
        steps = 0
        curr = k
        while curr != 1:
            steps += 1
            largest_power = math.log2(curr)
            if math.floor(largest_power) == largest_power:
                largest_power -= 1
            curr -= 2 ** math.floor(largest_power)
        return chr(ord('a') + steps % 26)