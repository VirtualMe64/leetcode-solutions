# Problem: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k
# Runtime: 493 ms

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = {}
        for num in arr:
            rem = num % k
            remainders[rem] = remainders.get(rem, 0) + 1
        
        for rem in remainders:
            needed = (k - rem) % k

            if needed == rem:
                if remainders[rem] % 2 == 1:
                    return False
            elif remainders[rem] != remainders.get(needed, 0):
                return False
        return True