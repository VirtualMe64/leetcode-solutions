# Problem: https://leetcode.com/problems/count-the-number-of-good-nodes
# Runtime: 4906 ms

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        numNodes = max(max([x[0] for x in edges], [x[1] for x in edges]))

        nbrs = [[] for _ in range(numNodes + 1)]
        for edge in edges:
            nbrs[edge[0]].append(edge[1])
            nbrs[edge[1]].append(edge[0])
        
        # step 1: bfs to get order
        order = []
        queue = [0]
        visited = set()
        while len(queue) > 0:
            curr = queue.pop(0)
            order.append(curr) 
            for nbr in nbrs[curr]:
                if nbr not in visited:
                    visited.add(curr)
                    queue.append(nbr)

        # traverse in reverse
        subtreeSizes = {}
        balancedCount = 0
        for edge in order[::-1]:
            counts = []
            for nbr in nbrs[edge]:
                if nbr in subtreeSizes:
                    counts.append(subtreeSizes[nbr]) 
            subtreeSizes[edge] = sum(counts) + 1

            if len(counts) == 0:
                balancedCount += 1
                continue

            balanced = True
            test = counts[0]
            for other in counts[1:]:
                if other != test:
                    balanced = False
                    break
            if balanced:
                balancedCount += 1

        return balancedCount