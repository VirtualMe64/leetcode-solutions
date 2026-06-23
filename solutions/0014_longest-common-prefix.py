# Problem: https://leetcode.com/problems/longest-common-prefix
# Runtime: 3 ms

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for s in strs[1:]:
            newLongest = ""
            for i in range(min(len(s), len(longest))):
                if longest[i] == s[i]:
                    newLongest += longest[i]
                else:
                    break
            longest = newLongest

        return longest