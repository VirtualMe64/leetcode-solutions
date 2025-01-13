# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters
# Runtime: 34 ms

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastSeenTable = {}
        length = 0
        longest = 0
        for i, char in enumerate(s):
            lastSeen = lastSeenTable.get(char, -1)
            lastSeenTable[char] = i
            if (i - lastSeen > length):
                length += 1
                longest = max(length, longest)
            else:
                length = i - lastSeen
        return longest