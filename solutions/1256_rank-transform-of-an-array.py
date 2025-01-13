# Problem: https://leetcode.com/problems/rank-transform-of-an-array
# Runtime: 267 ms

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)

        rank = {}
        idx = 1
        for num in sortedArr:
            if num in rank:
                continue
            rank[num] = idx
            idx += 1
        
        return [rank[n] for n in arr]