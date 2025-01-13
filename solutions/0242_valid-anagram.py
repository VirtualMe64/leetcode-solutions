# Problem: https://leetcode.com/problems/valid-anagram
# Runtime: 45 ms

class Solution(object):
    def canonical(self, word):
        curr = 0
        for char in word:
            curr += 1 << (7 * ord(char) - 96)
        return curr

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.canonical(s) == self.canonical(t)
        