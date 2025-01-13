# Problem: https://leetcode.com/problems/xor-queries-of-a-subarray
# Runtime: 317 ms

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        runningXor = [0 for i in range(len(arr) + 1)]
        for i, value in enumerate(arr):
            runningXor[i + 1] = runningXor[i] ^ value

        out = [runningXor[q[0]] ^ runningXor[q[1] + 1] for q in queries]
        return out