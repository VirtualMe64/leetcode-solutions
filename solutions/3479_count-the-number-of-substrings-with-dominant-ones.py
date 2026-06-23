# Problem: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones
# Runtime: 15770 ms

import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 0 -> 1
        # 1 -> 2
        # 2 -> 6
        # 3 -> 12
        # 4 -> 20


        zeros = []
        for i, c in enumerate(s):
            if c == '0':
                zeros.append(i)
        zeros.append(len(s))

        total = 0
        zeroIdx = 0
        for l in range(len(s)):
            while zeroIdx < len(zeros) and zeros[zeroIdx] < l:
                zeroIdx += 1

            if zeroIdx == len(zeros) - 1:
                # print("At end, adding:", len(s) - l)
                total += len(s) - l
                continue
                
            maxZeros = math.floor(math.sqrt(len(s) - l))
            for numZeros in range(maxZeros + 1):
                idx = zeroIdx + numZeros
                if idx + 1 > len(zeros):
                    break
                prevIdx = l if numZeros == 0 else zeros[idx - 1]
                nextIdx = zeros[idx]
                
                prev1s = prevIdx - l - numZeros + 1
                needed1s = max(numZeros ** 2 - prev1s, 0)
                new1s = nextIdx - prevIdx - 1
                total += max(new1s - needed1s + 1, 0)

                # print(l, numZeros, zeroIdx, prevIdx, nextIdx, prev1s, needed1s, new1s, max(new1s - needed1s + 1, 0))

        return total