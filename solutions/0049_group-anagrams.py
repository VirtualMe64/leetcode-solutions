# Problem: https://leetcode.com/problems/group-anagrams
# Runtime: 3734 ms

class Solution(object):
    def canonical(self, word):
        curr = 0
        for char in word:
            value = 1 << (7 * (ord(char) - 97))
            curr += value
        return curr

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
          return []
        groups = []
        for word in strs:
          rep = self.canonical(word)
          found = False
          for group in groups:
            if group[0] ^ rep == 0:
              group.append(word)
              found = True
              break
          if not found:
            groups.append([rep, word])
            
        return [x[1:] for x in groups]
