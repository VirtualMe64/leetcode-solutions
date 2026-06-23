# Problem: https://leetcode.com/problems/lexicographically-smallest-generated-string
# Runtime: 315 ms

from collections import deque

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        # if we shift str2 over i, does it overlap with itself?
        failureTable = []
        for i in range(len(str2) + 1):
            failureTable.append(str2[:i] == str2[len(str2)-i:])

        out = []
        str2Chars = [c for c in str2]
        idx = len(str2Chars)
        options = [chr(ord('a') + i) for i in range(26)]

        # for each char in the generated string
        for i in range(len(str1) + len(str2) - 1):
            if i < len(str1):
                # if still in str1 and T, next chars MUST be str2
                c = str1[i]
                if c == 'T':
                    if not failureTable[len(str2) - idx]:
                        # since prefix doesn't match suffix, impossible
                        return ""
                    else:
                        idx = 0

            # if char is fixed add it, otherwise fill it in later
            if idx < len(str2Chars):
                out.append(str2Chars[idx])
                idx += 1
            else:
                out.append(options.copy())

        for i, c in enumerate(out):
            if i >= len(str1) or str1[i] == 'T':
                continue
            # only consider words where str1 == F, since T is already accountde for

            word = out[i:i + len(str2)]
            option = None
            done = False

            for j, c in enumerate(word):
                # case 1: c is defined. If we don't match str2, F is satisfied no matter what!
                if isinstance(c, str):
                    if c != str2[j]:
                        done = True
                        break
                    continue

                # case 2: case 2: c is not fully defined
                # case 2a: if we can set c to min possible, just do that
                if str2[j] != min(c):
                    out[i + j] == min(c)
                    done = True
                    break
                # case 2b: take this as our furthest option
                option = (j, i + j, c)

            if not done:
                if option is None:
                    return ""
                idx1, idx2, vals = option
                vals.remove(str2[idx1])

                if len(vals) == 1:
                    out[idx2] = vals[0]
                else:
                    out[idx2] = vals
        
        for i, c in enumerate(out):
            # print(c)
            if isinstance(c, list):
                out[i] = min(c)
        
        return "".join(out)