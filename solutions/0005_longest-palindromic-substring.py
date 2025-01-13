# Problem: https://leetcode.com/problems/longest-palindromic-substring
# Runtime: 649 ms

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s)):
            curr = s[i]
            d = 1
            # odd
            while i - d >= 0 and i + d < len(s):
                c1 = s[i - d]
                c2 = s[i + d]
                if c1 != c2:
                    break
                if 2 * d + 1 > end - start:
                    start = i - d
                    end = i + d
                d += 1
            # even
            d = 0
            while i - d >= 0 and i + d + 1 < len(s):
                c1 = s[i - d]
                c2 = s[i + d + 1]
                if c1 != c2:
                    break
                if 2 * d + 2 > end - start:
                    start = i - d
                    end = i + d + 1
                d += 1
        return s[start : end + 1]
