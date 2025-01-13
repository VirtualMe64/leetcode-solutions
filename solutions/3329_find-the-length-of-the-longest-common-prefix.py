# Problem: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix
# Runtime: 795 ms

class Solution:
    def buildTrie(self, arr):
        trie = {}

        for num in arr:
            currTrie = trie
            for c in str(num):
                if c not in currTrie:
                    currTrie[c] = {}
                    currTrie = currTrie[c]
                else:
                    currTrie = currTrie[c]
        
        return trie

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie1 = self.buildTrie(arr1)
        
        longest = 0

        for num in arr2:
            length = 0
            currTrie = trie1
            for c in str(num):
                if c in currTrie:
                    length += 1
                    longest = max(length, longest)
                    currTrie = currTrie[c]
                else:
                    break
            
        return longest