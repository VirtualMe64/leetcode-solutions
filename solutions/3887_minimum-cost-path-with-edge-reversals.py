# Problem: https://leetcode.com/problems/minimum-cost-path-with-edge-reversals
# Runtime: 627 ms

import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = [[] for i in range(n)]

        for e in edges:
            edgeMap[e[0]].append((e[1], e[2]))
            edgeMap[e[1]].append((e[0], 2 * e[2]))

        # dijkstra
        dists = [float('inf') for i in range(n)]
        queue = []

        dists[0] = 0
        queue.append((0, 0)) # cost, vertex

        while len(queue) > 0:
            cost, vertex = heapq.heappop(queue)

            if cost > dists[vertex]:
                continue

            if vertex == n - 1:
                return cost

            for nbr in edgeMap[vertex]:
                newCost = cost + nbr[1]
                if newCost < dists[nbr[0]]:
                    dists[nbr[0]] = newCost
                    heapq.heappush(queue, (newCost, nbr[0]))

        return -1