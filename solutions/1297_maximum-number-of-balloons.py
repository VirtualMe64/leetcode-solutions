# Problem: https://leetcode.com/problems/maximum-number-of-balloons
# Runtime: 3 ms

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)

        return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])