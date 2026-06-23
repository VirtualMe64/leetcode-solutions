# Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# Runtime: 0 ms

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                break
        
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i

        return -1