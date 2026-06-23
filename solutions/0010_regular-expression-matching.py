# Problem: https://leetcode.com/problems/regular-expression-matching
# Runtime: 7 ms

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = []

        idx = 0
        while idx < len(p):
            c1 = p[idx]
            c2 = p[idx + 1] if idx + 1 < len(p) else ""

            if c2 == "*":
                pattern.append((c1, "*"))
                idx += 2
            else:
                pattern.append((c1, ""))
                idx += 1
        
        pattern = self.simplifyPattern(pattern)
        print(pattern)
        
        # store potential traversals in form (string idx, pattern idx)
        statusQueue = [(0, 0)]
        idx = 0

        while idx < len(statusQueue):
            stringIdx, patternIdx = statusQueue[idx]
            idx += 1

            if patternIdx >= len(pattern):
                if stringIdx >= len(s):
                    return True
                continue

            matcher = pattern[patternIdx]
            char = s[stringIdx] if stringIdx < len(s) else "EOF"
            atEof = char == "EOF"

            matches = matcher[0] == '.' or char == matcher[0]
            star = matcher[1] == "*"
            if matches and star:
                # two possibilities, use the star or dont
                if not atEof:
                    statusQueue.append((stringIdx + 1, patternIdx))
                statusQueue.append((stringIdx, patternIdx + 1))
            elif matches and not star:
                # one possibility: move on
                if not atEof:
                    statusQueue.append((stringIdx + 1, patternIdx + 1))
            elif not matches and star:
                # end the star here
                statusQueue.append((stringIdx, patternIdx + 1))

        return False

    def simplifyPattern(self, pattern):
        simplifiedPattern = []

        last = (None, None)

        for matcher in pattern:
            if last[1] == "*" and matcher[1] == "*":
                if last[0] == "." or last[0] == matcher[0]:
                    continue
            
            simplifiedPattern.append(matcher)
            last = matcher
        
        return simplifiedPattern