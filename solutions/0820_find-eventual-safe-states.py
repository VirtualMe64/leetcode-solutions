# Problem: https://leetcode.com/problems/find-eventual-safe-states
# Runtime: 57 ms

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # idea: reverse graph
        # every non cyclic path from a terminal node is safe
        reverseGraph = [[] for _ in range(len(graph))]
        outcount = {}
        queue = []
        safeNodes = set()
        for i, nbrs in enumerate(graph):
            outcount[i] = len(nbrs)
            if len(nbrs) == 0:
                queue.append(i)
            for nbr in nbrs:
                reverseGraph[nbr].append(i)

        while len(queue) > 0:
            curr = queue.pop(0)
            safeNodes.add(curr)

            for nbr in reverseGraph[curr]:
                outcount[nbr] -= 1
                if outcount[nbr] == 0:
                    queue.append(nbr)
        
        return sorted(list(safeNodes))