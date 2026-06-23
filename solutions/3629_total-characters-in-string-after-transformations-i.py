# Problem: https://leetcode.com/problems/total-characters-in-string-after-transformations-i
# Runtime: 524 ms

from collections import defaultdict

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = (10 ** 9) + 7

        # observation 1: each character is independent, sum size for each char
        # observation 2: 'a' + 26 = 'ab', 'b' + 26 = 'bc', 'z' + 26 = 'zab'
        # observation 3: 'a' + 25 = 'z' -- same length!
        # approach 1: keep dict of freq of each char, deal with t in units of 26 at a time
        counts = defaultdict(int)
        for c in s:
            counts[c] = counts[c] + 1

        while t >= 0:
            new_counts = counts.copy()
            for c, cnt in counts.items():
                # check if t is enough to force an overflow
                if (25 - (ord(c) - ord('a'))) >= t:
                    continue
                if c == 'z':
                    # if we aren't doing a full cycle, then only 2 chars made
                    if t < 26:
                        new_counts['z'] -= cnt
                    new_counts['a'] += cnt
                    new_counts['b'] += cnt
                    continue
                new_counts[chr(ord(c) + 1)] += cnt
            # for k, v in new_counts.items():
            #     new_counts[k] = v % MOD
            counts = new_counts
            t -= 26
        return sum(counts.values()) % MOD