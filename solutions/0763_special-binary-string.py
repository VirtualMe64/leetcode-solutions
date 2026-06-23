# Problem: https://leetcode.com/problems/special-binary-string
# Runtime: 15 ms

class Solution:
    def applyMove(self, s):
        best = s

        for i in range(len(s) - 1): # start of first part
            p2 = ""
            p2Count0 = 0
            p2Count1 = 0
            for j in range(i, len(s)): # current end of first part
                p2 += s[j]
                if s[j] == '1': p2Count1 += 1
                else:           p2Count0 += 1

                if p2Count0 > p2Count1:
                    break
                
                if p2Count0 == p2Count1: # p2 is special
                    p3 = ""
                    p3Count0 = 0
                    p3Count1 = 0

                    for k in range(j + 1, len(s)):
                        p3 += s[k]
                        if s[k] == '1': p3Count1 += 1
                        else:           p3Count0 += 1

                        if p3Count0 > p3Count1:
                            break
                        
                        if p3Count0 == p3Count1: # p3 is also special
                            v = s[:i] + p3 + p2 + s[k + 1:]
                            if v > best:
                                best = v

        return best

    def makeLargestSpecial(self, s: str) -> str:
        curr = s
        while True:
            modified = self.applyMove(curr)
            if modified == curr:
                return curr
            curr = modified