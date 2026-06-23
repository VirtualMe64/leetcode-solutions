# Problem: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix
# Runtime: 326 ms

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        longest = 0

        for n in arr1:
            s = str(n)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])
    
        for n in arr2:
            s = str(n)
            for i in range(longest + 1, len(s) + 1):
                pfx = s[:i]
                if pfx in prefixes:
                    longest = max(longest, len(pfx))
        
        return longest