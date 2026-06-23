# Problem: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii
# Runtime: 1741 ms

from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # if interval centered on number, count + others in range
        # if in between two numbers, window may as well have left value on a number
        # all findable with binary search

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        results = []
        runningSum = 0

        for num in sorted(counts.keys()):
            cnt = counts[num]
            results.append((num, runningSum, runningSum + cnt, cnt))
            runningSum += cnt

        best = 0

        # step 1: check ranges centered on numbers
        for num, _, _, cnt in results:
            left = num - k
            right = num + k

            leftIdx = bisect_left(results, left, key = lambda x : x[0])
            rightIdx = bisect_right(results, right, key = lambda x : x[0]) - 1

            leftVal = results[leftIdx][1]
            rightVal = results[rightIdx][2]

            base = cnt
            extra = rightVal - leftVal - base
            value = base + min(extra, numOperations)

            best = max(best, value)

        # step 2: check ranges starting on numbers
        for num, runningSum, _, _ in results:
            right = num + 2 * k
            rightIdx = bisect_right(results, right, key = lambda x : x[0]) - 1

            leftVal = runningSum
            rightVal = results[rightIdx][2]

            value = min(rightVal - leftVal, numOperations)
            best = max(best, value)
        
        return best