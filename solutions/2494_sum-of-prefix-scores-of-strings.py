# Problem: https://leetcode.com/problems/sum-of-prefix-scores-of-strings
# Runtime: 3880 ms

class Solution:
    def buildTrie(self, words):
        # build a trie which also counts frequency
        trie = {}

        for word in words:
            currTrie = trie
            for c in word:
                if c not in currTrie:
                    currTrie[c] = (1, {})
                    currTrie = currTrie[c][1]
                else:
                    currTrie[c] = (currTrie[c][0] + 1, currTrie[c][1])
                    currTrie = currTrie[c][1]

        return trie

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = self.buildTrie(words)

        answers = []
        for word in words:
            score = 0
            currTrie = trie
            for c in word:
                score += currTrie[c][0]
                currTrie = currTrie[c][1]
        
            answers.append(score)

        return answers