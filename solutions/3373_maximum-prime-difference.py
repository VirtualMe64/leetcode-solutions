# Problem: https://leetcode.com/problems/maximum-prime-difference
# Runtime: 857 ms

from math import ceil

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        firstPrime = None
        best = None
        for i, n in enumerate(nums):
            if self.isPrime(n):
                if firstPrime is None:
                    firstPrime = i
                    best = 0
                else:
                    best = i - firstPrime
        return best

    def isPrime(self, n):
        if n <= 1:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False
        
        for i in range(3, ceil(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        
        return True