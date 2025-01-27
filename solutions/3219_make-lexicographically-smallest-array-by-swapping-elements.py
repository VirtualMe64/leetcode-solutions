# Problem: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements
# Runtime: 460 ms

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Observation: we can fully rearrange any 'chain' of numberes
        # Partition nums into sets which are limit chain, sort chains
        # Find these partitions efficiently by sorting

        sortedIndexed = sorted(enumerate(nums), key = lambda x : x[1])
        partitions = []
        currPartition = []

        for i, num in sortedIndexed:
            # start or extend the partition
            if len(currPartition) == 0 or (num - currPartition[-1][1]) <= limit:
                currPartition.append((i, num))
            else:
                partitions.append(currPartition)
                currPartition = [(i, num)]
        partitions.append(currPartition)

        out = [None for i in range(len(nums))]
        for p in partitions:
            numOrder = sorted(p, key = lambda x : x[1])
            idxOrder = sorted(p, key = lambda x : x[0])
            for i in range(len(p)):
                out[idxOrder[i][0]] = numOrder[i][1]
        return out