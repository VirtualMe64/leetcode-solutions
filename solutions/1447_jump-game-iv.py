# Problem: https://leetcode.com/problems/jump-game-iv
# Runtime: 131 ms

from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0

        teleports = {}

        for i, v in enumerate(arr):
            if v not in teleports:
                teleports[v] = []
            teleports[v].append(i)

        costs = [float('inf') for _ in range(len(arr))]
        costs[-1] = 0
        dfs = deque([len(arr) - 1])
        while len(dfs) > 0:
            idx = dfs.popleft()
            cost = costs[idx]

            otherIndices = [idx + 1, idx - 1]
            if arr[idx] in teleports:
                otherIndices.extend(teleports[arr[idx]])
                del teleports[arr[idx]]

            for otherIdx in otherIndices:
                if otherIdx >= 0 and otherIdx < len(arr) and cost + 1 < costs[otherIdx]:
                    costs[otherIdx] = cost + 1
                    dfs.append(otherIdx)

                    if otherIdx == 0:
                        return cost + 1