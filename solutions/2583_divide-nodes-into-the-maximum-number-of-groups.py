# Problem: https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups
# Runtime: 2553 ms

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # observation: a 3 cycle is impossible
        # observation: any odd cycle is impossible
        # maybe related to bipartite graphs?
        # simplest approach: dfs with clock
        # is graph guaranteed to be connected?
        # a: no -- solve for each component separately
        # problem: value depends on which node we start from
        # solution: try all starting nodes
        edgeMap = [[] for i in range(n)]
        for e in edges:
            edgeMap[e[0] - 1].append(e[1] - 1)
            edgeMap[e[1] - 1].append(e[0] - 1)
       
        components = []
        visited = set()
        queue = []
        for i in range(n):
            if i in visited:
                continue
            comp = []
            queue.append(i)
            visited.add(i)
            while len(queue) > 0:
                curr = queue.pop(-1)
                comp.append(curr)
                for nbr in edgeMap[curr]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)
            components.append(comp)
        total = 0
        for c in components:
            res = self.solveComponent(c, edgeMap)
            if res == -1: # unsolvable component
                return -1
            total += res
        return total

    def solveComponent(self, edges, edgeMap):
        best = None
        for start in edges:
            clock = 1
            groups = {start: 1}
            queue = [start]
            while len(queue) > 0:
                curr = queue.pop(0)
                currClock = groups[curr]
                for nbr in edgeMap[curr]:
                    if nbr in groups:
                        if (groups[nbr] % 2) == (currClock % 2):
                            return -1 # odd cycle -- impossible!
                    else:
                        groups[nbr] = currClock + 1
                        clock = max(clock, currClock + 1)
                        queue.append(nbr)
            best = clock if best is None else max(best, clock)
        return best