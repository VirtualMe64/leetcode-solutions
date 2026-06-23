# Problem: https://leetcode.com/problems/sum-of-distances
# Runtime: 105 ms

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indicesByNum = {}
        for i, n in enumerate(nums):
            if n not in indicesByNum:
                indicesByNum[n] = []
            indicesByNum[n].append(i)

        arr = [None for i in range(len(nums))]

        for v in indicesByNum.values():
            totalLeft = sum(v)
            numLeft = len(v)
            totalSeen = 0
            numSeen = 0
            
            prev = 0
            for i in v:
                delta = i - prev
                totalSeen += numSeen * delta
                numSeen += 1
                totalLeft -= numLeft * delta
                numLeft -= 1

                arr[i] = totalSeen + totalLeft

                prev = i

        return arr