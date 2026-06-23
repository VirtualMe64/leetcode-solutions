# Problem: https://leetcode.com/problems/unique-length-3-palindromic-subsequences
# Runtime: 627 ms

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        starts = {}
        ends = {}

        for i, c in enumerate(s):
            if c not in starts:
                starts[c] = i
            else:
                ends[c] = i
        
        starts = {i: c for c, i in starts.items() if c in ends}
        ends = {i: c for c, i in ends.items()}

        active = set()
        alphabets = {}
        total = 0

        for i, c in enumerate(s):
            if i in ends:
                active.remove(ends[i])
                total += len(alphabets[ends[i]])

            for a in active:
                alphabets[a].add(c)

            if i in starts:
                alphabets[starts[i]] = set()
                active.add(starts[i])
        
        return total