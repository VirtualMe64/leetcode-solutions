# Problem: https://leetcode.com/problems/minimum-absolute-difference
# Runtime: 73 ms

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDist = min(abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1))
        arrSet = set(arr)

        out = []
        for i in arr:
            if i + minDist in arrSet:
                out.append([i, i + minDist])
        return out