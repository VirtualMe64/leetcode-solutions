# Problem: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations
# Runtime: 139 ms

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # source can be partitioned into regions in which elements can be swapped
        # disjoint set vibes
        parents = [i for i in range(len(source))] # at first, every element is it's own parent
        
        def find(i):
            if parents[i] == i:
                return i

            parent = find(parents[i])
            parents[i] = parent
            return parent
        
        for swap in allowedSwaps:
            v1 = find(swap[0])
            v2 = find(swap[1])
            parents[v2] = v1

        partitions = {}

        for i in range(len(source)):
            v = find(i)
            if v not in partitions:
                partitions[v] = [i]
            else:
                partitions[v].append(i)

        totalDist = 0
        
        # since we can move values freely in a partition, cost is number of unpaired elements
        for p in partitions.values():
            counts = {}
            # first sweep: get counts in target
            for i in p:
                v = target[i]
                counts[v] = counts.get(v, 0) + 1
            
            # second sweep: mach with source
            for i in p:
                v = source[i]
                if v in counts and counts[v] > 0:
                    counts[v] -= 1
                else:
                    totalDist += 1

        return totalDist