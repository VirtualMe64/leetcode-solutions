# Problem: https://leetcode.com/problems/decode-ways
# Runtime: 45 ms

class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 1
        prev1 = 0 if s[0] == '0' else 1

        for i in range(len(s) - 1):
            s1 = s[i + 1]
            s2 = s[i : i + 2]

            out = 0 if s1 == '0' else prev1
            s2Valid = s2[0] != '0' and 0 <= int(s2) <= 26

            if s2Valid:
                out += prev2
            prev2 = prev1
            prev1 = out
        
        return prev1