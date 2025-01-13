# Problem: https://leetcode.com/problems/find-if-array-can-be-sorted
# Runtime: 14 ms

class Solution:
    def numBits(self, num):
        total = 0
        while num > 0:
            total += num & 1
            num >>= 1
        return total

    def canSortArray(self, nums: List[int]) -> bool:
        # question is, is there a larger number to the left
        # with different number of set bits
        # if so, we cannot sort it!

        # naive: O(n^2), check every other num in the range
        # better: keep track of largest number by bit count
        # now (n * nuniqueBitCounts)
        largest = {}

        for num in nums:
            bits = self.numBits(num)

            for otherBits, val in largest.items():
                if otherBits != bits and val > num:
                    return False 

            largest[bits] = max(largest.get(bits, 0), num)

        return True