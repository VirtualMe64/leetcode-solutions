# Problem: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i
# Runtime: 663 ms

from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # observation: for given depth d, 2^(d - 1) paths
        # so find max depth, return 2^(d - 1)
        n = len(edges) + 1

        edgeDict = {v : [] for v in range(n)}
        for e in edges:
            edgeDict[e[0] - 1].append(e[1] - 1)
            edgeDict[e[1] - 1].append(e[0] - 1)

        maxDepth = 0
        queue = deque([(0, 0)])
        visited = set()
        while queue:
            curr, depth = queue.popleft()
            visited.add(curr)
            
            for nbr in edgeDict[curr]:
                if nbr in visited:
                    continue
                
                maxDepth = max(maxDepth, depth + 1)
                queue.append((nbr, depth + 1))

        if maxDepth == 0:
            return 0
        
        return pow(2, maxDepth - 1, 10 ** 9 + 7)