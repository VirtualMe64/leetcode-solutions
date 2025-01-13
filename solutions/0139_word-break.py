# Problem: https://leetcode.com/problems/word-break
# Runtime: 41 ms

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxLen = max(len(w) for w in wordDict)
        wordSet = set(wordDict)
        frontier = [s]
        visited = set()

        # DFS
        while len(frontier) > 0:
            word = frontier.pop()
            if len(word) == 0:
                return True
            for i in range(maxLen, 0, -1):
                if word[0:i] in wordSet:
                    potential = word[i:]
                    if potential not in visited:
                        visited.add(potential)
                        frontier.append(potential)
        
        return False