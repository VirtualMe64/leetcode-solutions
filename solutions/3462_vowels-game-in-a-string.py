# Problem: https://leetcode.com/problems/vowels-game-in-a-string
# Runtime: 68 ms

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # losing state (for alice): no vowels (including empty string)
        # losing state (for bob): 1 vowel or empty string
        
        # observation 0: no vowels means alice loses
        # observation 1: even number of vowels means alice wins (remove all but 1, remove whole string next turn)
        # observation 2: odd number of vowels  means alice wins (remove the whole string)
        # so if there's any vowels alice wins??
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for c in s:
            if c in vowels:
                return True
        return False