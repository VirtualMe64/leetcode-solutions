# Problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target
# Runtime: 0 ms

from bisect import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        fst = letters[0]
        letters.sort()

        idx = bisect(letters, target)
        
        return letters[idx] if idx < len(letters) else fst