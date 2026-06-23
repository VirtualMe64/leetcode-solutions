# Problem: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii
# Runtime: 352 ms

import bisect

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # store the 3 biggest gaps
        biggestGaps = [startTime[0]]

        for i in range(len(endTime)):
            gapStart = endTime[i]
            gapEnd = startTime[i + 1] if i + 1 < len(startTime) else eventTime

            gapSize = gapEnd - gapStart
            if len(biggestGaps) < 3:
                biggestGaps.append(gapSize)
            elif gapSize > min(biggestGaps):
                biggestGaps.remove(min(biggestGaps))
                biggestGaps.append(gapSize)

        maxFreeTime = 0

        for i in range(len(endTime)):
            leftGapStart = 0 if i == 0 else endTime[i - 1]
            start = startTime[i]
            end = endTime[i]
            rightGapEnd = startTime[i + 1] if i + 1 < len(startTime) else eventTime

            leftGapSize = start - leftGapStart
            rightGapSize = rightGapEnd - end
            meetingLength = end - start

            possibleGaps = [x for x in biggestGaps]
            if leftGapSize in possibleGaps: possibleGaps.remove(leftGapSize)
            if rightGapSize in possibleGaps: possibleGaps.remove(rightGapSize)

            size = leftGapSize + rightGapSize
            if max(possibleGaps) >= meetingLength:
                size += meetingLength
            
            maxFreeTime = max(maxFreeTime, size)

        return maxFreeTime