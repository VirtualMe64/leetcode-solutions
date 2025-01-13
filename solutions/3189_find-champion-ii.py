# Problem: https://leetcode.com/problems/find-champion-ii
# Runtime: 14 ms

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champions = set([i for i in range(n)])
        for e in edges:
            if e[1] in champions:
                champions.remove(e[1])
        return -1 if len(champions) > 1 else list(champions)[0]