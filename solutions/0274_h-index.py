# Problem: https://leetcode.com/problems/h-index
# Runtime: 0 ms

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        # 0 1 3 6 5
        for i, cnt in enumerate(citations):
            h = len(citations) - i
            if cnt >= h:
                return h

        return 0