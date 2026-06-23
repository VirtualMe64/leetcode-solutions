# Problem: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon
# Runtime: 1281 ms

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxEnergy = None
        dpTable = [0 for i in range(k)]

        for i in range(len(energy)):
            idx = len(energy) - i - 1
            dpIdx = i % k

            dp = dpTable[dpIdx]
            val = energy[idx] + dp

            maxEnergy = max(maxEnergy, val) if maxEnergy is not None else val
            dpTable[dpIdx] = val
        
        return maxEnergy