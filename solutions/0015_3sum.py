# Problem: https://leetcode.com/problems/3sum
# Runtime: 2535 ms

class Solution:
    def twoSum(self, nums, startIdx, target):
        seen = set()
        pairs = set()

        for i in range(startIdx, len(nums)):
            n = nums[i]
            needed = target - n
            if needed in seen:
                v1 = n
                v2 = needed
                pairs.add((min(v1, v2), max(v1, v2)))

            seen.add(n)

        
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def canonize(v1, v2, v3):
            return tuple(sorted([v1, v2, v3]))

        triplets = set()
        for i, n in enumerate(nums):
            for other in self.twoSum(nums, i + 1, -n):
                triplets.add(canonize(n, other[0], other[1]))
        
        return list(triplets)