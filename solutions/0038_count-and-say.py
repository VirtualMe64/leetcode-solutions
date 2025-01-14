# Problem: https://leetcode.com/problems/count-and-say
# Runtime: 0 ms

class Solution:
    cache = {}
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        if n in self.cache:
            return self.cache[n]

        base = self.countAndSay(n - 1)
        
        out = []
        currDigit = ""
        currCount = -1
        for c in base:
            if c != currDigit:
                if currDigit != "":
                    out.append(str(currCount))
                    out.append(currDigit)
                currDigit = c
                currCount = 1
            else:
                currCount += 1
        out.append(str(currCount))
        out.append(currDigit)
        s = "".join(out)
        self.cache[n] = s
        return s