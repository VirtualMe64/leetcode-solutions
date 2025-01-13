# Problem: https://leetcode.com/problems/longest-square-streak-in-an-array
# Runtime: 181 ms

class Solution:
    def getBase(self, num, depth):
        root = num ** 0.5
        if root != int(root):
            return num, depth
        else:
            return self.getBase(root, depth + 1)

    def longestRun(self, arr):
        if len(arr) <= 1:
            return len(arr)
        best = 1
        curr = 1
        sortedArr = sorted(arr)
        for i in range(1, len(arr)):
            if sortedArr[i] == sortedArr[i - 1] + 1:
                curr += 1
            else:
                curr = 0
            best = max(best, curr)
        return best

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = list(set(nums))
        occurences = {}

        for num in nums:
            val, depth = self.getBase(num, 1)
            occurences[val] = occurences.get(val, []) + [depth]
        
        best = 0
        for arr in occurences.values():
            best = max(best, self.longestRun(arr))

        # print(occurences)
        return best if best > 1 else -1