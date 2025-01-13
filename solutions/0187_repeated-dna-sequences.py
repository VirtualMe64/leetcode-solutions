# Problem: https://leetcode.com/problems/repeated-dna-sequences
# Runtime: 62 ms

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        out = set()

        curr = ""
        for c in s:
            if len(curr) < 9:
                curr = curr + c
                continue
            curr = curr + c
            if len(curr) > 10:
                curr = curr[-10:]
            if curr in seen:
                out.add(curr)
            else:
                seen.add(curr)
        return list(out)