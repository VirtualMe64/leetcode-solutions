# Problem: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks
# Runtime: 52 ms

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # idea 1: choose greedily by excess energy
        tasks.sort(key = lambda x : x[1] - x[0])
        
        totalEnergy = 0
        maxExcess = 0
        for t in tasks:
            totalEnergy += t[0]
            excessEnergy = t[1] - totalEnergy
            maxExcess = max(maxExcess, excessEnergy)
        
        return totalEnergy + maxExcess