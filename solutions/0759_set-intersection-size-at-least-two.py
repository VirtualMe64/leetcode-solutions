# Problem: https://leetcode.com/problems/set-intersection-size-at-least-two
# Runtime: 12 ms

from bisect import bisect_left

class OverlappingInterval:
    def __init__(self, interval):
        self.start = interval[0]
        self.end = interval[1]
        self.intervals = [interval]

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], x[1]))

        total = 2

        #   rem1Ptr      rem2Ptr       i
        #      v           v           v
        # [a b c d e f g h i j k l m n o p q r s t u v w x y z]

        rem2Ptr = 0
        minEnd2 = intervals[0][1]
        ends2 = set([minEnd2])
        rem1Ptr = 0
        minEnd1 = intervals[0][1]

        for i in range(1, len(intervals)):
            oi = intervals[i]

            if oi[0] > minEnd2:
                total += 2
                rem1Ptr = i
                minEnd1 = oi[1]
                rem2Ptr = i
                minEnd2 = oi[1]
                ends2 = set([minEnd2])
            elif oi[0] > minEnd1 or oi[0] in ends2:
                total += 1
                rem1Ptr = rem2Ptr
                minEnd1 = minEnd2
                rem2Ptr = i
                minEnd2 = oi[1]
                ends2 = set([minEnd2])
            else:
                minEnd2 = min(minEnd2, oi[1])
                ends2.add(oi[1])

        return total