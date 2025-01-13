# Problem: https://leetcode.com/problems/longest-happy-string
# Runtime: 3 ms

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        rem = [a, b, c]
        chars = ['a', 'b', 'c']

        out = ""
        currCount = 0
        currLetter = None

        while True:
            effectiveRem = [x if currCount < 2 or currLetter != chars[i] else 0 for i, x in enumerate(rem)]
            # first check -- max rem
            best = max(effectiveRem)
            if best == 0:
                break

            options = [i for i in range(len(rem)) if effectiveRem[i] == best]
            letter = chars[options[0]]
            if currLetter == letter:
                currCount += 1
            else:
                currCount = 1
            currLetter = letter
            out += letter
            rem[options[0]] -= 1

        return out