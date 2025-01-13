# Problem: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
# Runtime: 0 ms

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        targetLen = len(searchWord)

        for i, s in enumerate(sentence.split(" ")):
            if s[0:targetLen] == searchWord:
                return i + 1

        return -1