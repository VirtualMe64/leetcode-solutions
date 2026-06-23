# Problem: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations
# Runtime: 20 ms

MOD = 10 ** 9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if len([c for c in complexity if c <= complexity[0]]) > 1:
            return 0
        
        curr = 1
        for i in range(1, len(complexity)):
            curr *= i
            curr %= MOD
        return curr