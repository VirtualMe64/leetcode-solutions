# Problem: https://leetcode.com/problems/weighted-word-mapping
# Runtime: 12 ms

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def inverseWeight(n):
            return chr(25 - n + ord('a'))

        def convert(word):
            totalWeight = sum([weights[ord(c) - ord('a')] for c in word])
            return inverseWeight(totalWeight % 26)
        
        return "".join([convert(w) for w in words])