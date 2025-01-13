# Problem: https://leetcode.com/problems/convert-date-to-binary
# Runtime: 40 ms

class Solution:
    def numToBin(self, num : int):
        out = ""
        while num > 0:
            out = str(num & 1) + out
            num = num >> 1
        return out

    def convertDateToBinary(self, date: str) -> str:
        return "-".join([self.numToBin(int(x)) for x in date.split("-")])        