# Problem: https://leetcode.com/problems/zigzag-conversion
# Runtime: 59 ms

class Solution:
    # period = numRows down + (numRows - 2) diagonal up
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        period = numRows + numRows - 2
        outStr = ""
        for currRow in range(numRows):
            periodIndices = []
            if currRow == 0 or currRow == numRows - 1:
                periodIndices = [currRow]
            else:
                periodIndices = [currRow, period - currRow]
            currIter = 0
            while True:
                nextIndex = periodIndices[currIter]
                if nextIndex >= len(s):
                    break
                outStr += s[nextIndex]
                periodIndices[currIter] += period
                currIter += 1
                currIter %= len(periodIndices)

        return outStr
