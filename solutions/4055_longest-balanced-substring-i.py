# Problem: https://leetcode.com/problems/longest-balanced-substring-i
# Runtime: 2950 ms

from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            counts = {}
            byCount = defaultdict(set)
            for j in range(i, len(s)):
                c = s[j]

                if c in counts:
                    byCount[counts[c]].remove(c)
                    if len(byCount[counts[c]]) == 0:
                        del byCount[counts[c]]
                    counts[c] += 1
                    byCount[counts[c]].add(c)
                else:
                    byCount[1].add(c)
                    counts[c] = 1
                
                if len(byCount) == 1:
                    longest = max(longest, j - i + 1)
        
        return longest