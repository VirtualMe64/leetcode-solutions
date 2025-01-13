# Problem: https://leetcode.com/problems/remove-k-digits
# Runtime: 418 ms

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 12345623

        removals = k
        currIndex = 0
        currStr = num
        while removals > 0 and currIndex < len(num):
            if currIndex == len(currStr) - 1:
                currIndex -= 1
                removals -= 1
                currStr = currStr[:-1]
                continue
            remove = currStr[currIndex] > currStr[currIndex + 1]
            if not remove:
                currIndex += 1
                continue
            # remove and update indices
            currStr = currStr[0 : currIndex] + currStr[currIndex + 1:]
            currIndex = 0 if currIndex == 0 else currIndex - 1
            removals -= 1

        out = ""
        seenNonZero = False
        for c in currStr:
            seenNonZero |= c != '0'
            if seenNonZero:
                out += c

        return out if out != '' else '0'