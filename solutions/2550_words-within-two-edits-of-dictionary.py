# Problem: https://leetcode.com/problems/words-within-two-edits-of-dictionary
# Runtime: 6 ms

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def checkQuery(q):
            for w in dictionary:
                strikes = 0
                for i in range(len(w)):
                    if w[i] != q[i]:
                        strikes += 1
                    if strikes == 3:
                        break
                else:
                    return True
            return False

        out = []
        for q in queries:
            if checkQuery(q):
                out.append(q)
        return out