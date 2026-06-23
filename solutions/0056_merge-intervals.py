# Problem: https://leetcode.com/problems/merge-intervals
# Runtime: 12 ms

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        out = []
        intervalStart = intervals[0][0]
        intervalEnd = intervals[0][1]

        for interval in intervals:
            if interval[0] > intervalEnd:
                out.append([intervalStart, intervalEnd])
                intervalStart, intervalEnd = interval[0], interval[1]
            else:
                intervalEnd = max(intervalEnd, interval[1])
        
        out.append([intervalStart, intervalEnd])

        return out