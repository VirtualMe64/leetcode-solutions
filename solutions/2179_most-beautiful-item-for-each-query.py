# Problem: https://leetcode.com/problems/most-beautiful-item-for-each-query
# Runtime: 217 ms

class Solution:
    def binSearch(self, items, q):
        left = 0
        right = len(items) - 1

        while left < right:
            mid = (left + right + 1) // 2
            if items[mid][0] == q:
                return items[mid][1]
            if items[mid][0] < q:
                left = mid
            else:
                right = mid - 1
        return items[left][1]

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x : x[0])

        dedupedItems = []

        best = 0
        lastCost = 0
        for item in items:
            if item[1] > best:
                best = item[1]
            item[1] = best

            if item[0] == lastCost:
                dedupedItems[-1][1] = best
            else:
                dedupedItems.append(item)

            lastCost = item[0]

        out = []
        for q in queries:
            if q < dedupedItems[0][0]:
                out.append(0)
            else:
                out.append(self.binSearch(dedupedItems, q))
        return out