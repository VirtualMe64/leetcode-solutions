# Problem: https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations
# Runtime: 426 ms

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def rotate(s):
            part1 = s[:b]
            part2 = s[b:]

            return part2 + part1
        
        rotateMap = {}
        for i in range(0, 10):
            rotated = (i + a) % 10
            rotateMap[str(i)] = str(rotated)

        def addToOddIndices(s):
            out = []
            for i, c in enumerate(s):
                if i % 2 == 1:
                    out.append(rotateMap[c])
                else:
                    out.append(c)
    
            return ''.join(out)

        visited = set([s])
        queue = [s]
        best = s

        while len(queue) > 0:
            curr = queue.pop(-1)

            nbr1 = rotate(curr)
            nbr2 = addToOddIndices(curr)

            for nbr in [nbr1, nbr2]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
                    if nbr < best:
                        best = nbr
        
        return best