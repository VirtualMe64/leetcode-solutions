# Problem: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii
# Runtime: 135 ms

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def earliestFinishTimeHelper(start1, dur1, start2, dur2):
            earliestEnd = inf

            for i in range(len(start1)):
                earliestEnd = min(earliestEnd, start1[i] + dur1[i])
            
            out = inf

            for j in range(len(start2)):
                finishTime = max(earliestEnd, start2[j]) + dur2[j]
                out = min(out, finishTime)
            
            return out
        
        return min(
            earliestFinishTimeHelper(landStartTime, landDuration, waterStartTime, waterDuration),
            earliestFinishTimeHelper(waterStartTime, waterDuration, landStartTime, landDuration)
        )