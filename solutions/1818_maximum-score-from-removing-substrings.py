# Problem: https://leetcode.com/problems/maximum-score-from-removing-substrings
# Runtime: 4189 ms

class Solution:
    def evaluateSegment(self, seg, x, y):
        # print(f"Evaluating seg {seg}")
        # idea 1: greedy
        if x > y: # remove the ab substrings
            target = 'ab'
            val = x
        else:
            target = 'ba'
            val = y
        score = 0
        while target in seg:
            # print(target, val, seg, score + val)
            seg = seg.replace(target, '', 1)
            score += val
        target = 'ab' if target == 'ba' else 'ba'
        val = x if val == y else y
        while target in seg:
            # print(target, val, seg, score + val)
            seg = seg.replace(target, '', 1)
            score += val
        # print(f"Got score {score}")
        return score

    def maximumGain(self, s: str, x: int, y: int) -> int:
        total = 0

        run = ""
        for c in s:
            if c == 'a' or c == 'b':
                run += c
            elif len(run) > 1:
                total += self.evaluateSegment(run, x, y)
                run = ""
            else:
                run = ""
        if len(run) > 1:
            total += self.evaluateSegment(run, x, y)

        return total                