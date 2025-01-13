# Problem: https://leetcode.com/problems/optimal-partition-of-string
# Runtime: 89 ms

class Solution:
    def partitionString(self, s: str) -> int:
        curr = set()
        partitions = 1
        for char in s:
            if char in curr:
                curr = set()
                partitions += 1
            curr.add(char)
        return partitions