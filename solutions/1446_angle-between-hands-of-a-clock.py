# Problem: https://leetcode.com/problems/angle-between-hands-of-a-clock
# Runtime: 0 ms

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourFrac = (((hour  % 12) * 60) + minutes) / (60 * 12)
        hourDegs = hourFrac * 360
        minuteFrac = minutes / 60
        minuteDegs = minuteFrac * 360

        angle1 = abs(hourDegs - minuteDegs)
        angle2 = hourDegs + (360 - minuteDegs)
        angle3 = minuteDegs + (360 - hourDegs)
        return min(angle1, angle2, angle3)