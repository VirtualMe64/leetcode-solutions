# Problem: https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements
# Runtime: 323 ms

class Solution:
    def findScore(self, nums: List[int]) -> int:
        numbered = [(i, x) for i, x in enumerate(nums)]
        numbered.sort(key = lambda x : x[1]) # stable, so index is kept

        seen = set()

        score = 0
        ptr = 0

        while ptr < len(numbered):
            currIdx, currVal = numbered[ptr]
            ptr += 1
            if currIdx in seen:
                continue
            score += currVal
            seen.add(currIdx)
            seen.add(currIdx + 1)
            seen.add(currIdx - 1)

        return score