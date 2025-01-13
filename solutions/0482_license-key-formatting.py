# Problem: https://leetcode.com/problems/license-key-formatting
# Runtime: 53 ms

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        out = []

        count = 0
        for c in s[::-1]:
            if c == "-":
                continue
            out.append(c.upper())
            count += 1

            if count == k:
                out.append("-")
                count = 0

        if len(out) == 0:
            return ""
        if out[-1] == "-":
            out = out[:-1]
        return "".join(out[::-1])