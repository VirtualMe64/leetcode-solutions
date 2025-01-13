# Problem: https://leetcode.com/problems/substring-with-concatenation-of-all-words
# Runtime: 7200 ms

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freqs = {}
        for word in words:
            word_freqs[word] = word_freqs.get(word, 0) + 1

        # idea 1: BFS
        # probably should memoize somehow -- maybe go in reverse?
        needed_len = len(words) * len(words[0])

        indices = []

        for start in range(0, len(s) - needed_len + 1):
            if self.dfs(s, word_freqs, start, len(words), len(words[0])):
                indices.append(start)
        
        return indices

    def dfs(self, s, word_freqs, start, n_words, word_len):
        curr_idx = start
        curr_freqs = {word : 0 for word in word_freqs.keys()}

        for i in range(n_words):
            substr = s[curr_idx : curr_idx + word_len]
            if substr not in word_freqs:
                return False
            if curr_freqs[substr] >= word_freqs[substr]:
                return False
            curr_idx += word_len
            curr_freqs[substr] += 1
        return True