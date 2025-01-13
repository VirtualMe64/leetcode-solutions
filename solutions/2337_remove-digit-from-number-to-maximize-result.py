# Problem: https://leetcode.com/problems/remove-digit-from-number-to-maximize-result
# Runtime: 40 ms

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = None
        for i, char in enumerate(number):
            if char == digit:
                option = number[0 : i] + number[i + 1:]
                if best == None or option > best:
                    best = option
        return best