# Problem: https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions
# Runtime: 13665 ms

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        endTimes = [0 for i in range(len(skill))]

        for p in mana:
            end = 0
            for i in range(len(skill)):
                brewTime = skill[i] * p
                end = max(end, endTimes[i]) + brewTime
            
            for i in range(len(endTimes)):
                idx = len(endTimes) - i - 1
                endTimes[idx] = end
                end -= skill[idx] * p

        return endTimes[-1]