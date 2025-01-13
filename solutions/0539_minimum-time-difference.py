# Problem: https://leetcode.com/problems/minimum-time-difference
# Runtime: 73 ms

class Solution:
    def timeToMinutes(self, time):
        return int(time[0:2]) * 60 + int(time[3:])

    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [self.timeToMinutes(t) for t in timePoints]
        times.sort()

        best = times[0] + (24 * 60) - times[-1]
    
        for i in range(len(times) - 1):
            delta = times[i + 1] - times[i]
            best = min(best, delta)
        
        return best