# Problem: https://leetcode.com/problems/add-binary
# Runtime: 0 ms

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = []

        aIdx = len(a) - 1
        bIdx = len(b) - 1
        carry = 0

        while aIdx >= 0 or bIdx >= 0:
            aVal = int(a[aIdx]) if aIdx >= 0 else 0
            bVal = int(b[bIdx]) if bIdx >= 0 else 0

            sum3 = aVal + bVal + carry
            out.append(str(sum3 % 2))
            carry = 1 if sum3 >= 2 else 0

            aIdx -= 1
            bIdx -= 1

        out.append(str(carry))

        outS = ""
        started = False
        for c in out[::-1]:
            if c == "1":
                started = True
            if started:
                outS += c
    
        return outS if started else "0"