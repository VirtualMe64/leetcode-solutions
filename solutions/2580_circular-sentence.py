# Problem: https://leetcode.com/problems/circular-sentence
# Runtime: 0 ms

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        parts = sentence.split(" ")

        if sentence[0] != sentence[-1]:
            return False

        for i in range(len(parts) - 1):
            if parts[i][-1] != parts[i + 1][0]:
                return False
        
        return True