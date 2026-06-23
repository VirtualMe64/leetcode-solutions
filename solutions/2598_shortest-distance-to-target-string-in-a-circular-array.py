# Problem: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array
# Runtime: 0 ms

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        shortest = None

        for i, word in enumerate(words):
            if word != target:
                continue
            
            rightDist = i - startIndex if i >= startIndex else len(words) - startIndex + i
            leftDist = startIndex - i if startIndex >= i else len(words) - i + startIndex
            dist = min(leftDist, rightDist)
            shortest = min(shortest, dist) if shortest is not None else dist

        return shortest if shortest is not None else -1