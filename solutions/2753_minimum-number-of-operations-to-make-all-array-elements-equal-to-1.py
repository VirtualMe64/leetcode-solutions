# Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1
# Runtime: 0 ms

def gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # [(2, 3), (2, 5), (3, 5)]

        count1s = nums.count(1)
        if count1s > 0:
            return len(nums) - count1s

        arr = nums
        depth = 0

        while len(arr) > 1:
            newArr = []
            for i in range(len(arr) - 1):
                val = gcd(arr[i], arr[i + 1])
                if val == 1:
                    return len(nums) + depth
                newArr.append(val)
            depth += 1
            arr = newArr
        
        return -1