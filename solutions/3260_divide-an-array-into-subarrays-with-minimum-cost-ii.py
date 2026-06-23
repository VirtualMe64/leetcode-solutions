# Problem: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii
# Runtime: 1318 ms

from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # question is equivalent to finding the maximum sum of (k-1) values
        # in a window of size dist + 1 (only considering nums[1:])
        # can solve this with two sorted lists, one for upper values one for lower

        topList = SortedList([])
        topListSum = 0
        bottomList = SortedList([])

        first = nums[0]
        nums = nums[1:]

        best = float('inf')
        for i in range(len(nums)):
            if i >= dist + 1:
                prev = nums[i - (dist + 1)]
                if prev <= topList[-1]:
                    topList.remove(prev)
                    topListSum -= prev
                    if len(bottomList) > 0:
                        topList.add(bottomList[0])
                        topListSum += bottomList[0]
                        bottomList.pop(0)
                else:
                    bottomList.remove(prev)
            
            if i < len(nums):
                n = nums[i]
    
                if len(topList) < k - 1:
                    topList.add(n)
                    topListSum += n
                elif n < topList[-1]:
                    rem = topList[-1]
                    topList.pop(-1)
                    topListSum -= rem
                    topList.add(n)
                    topListSum += n
                    bottomList.add(rem)
                else:
                    bottomList.add(n)

            if len(topList) >= k - 1:
                best = min(best, topListSum)

        return first + best