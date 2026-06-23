# Problem: https://leetcode.com/problems/majority-element-ii
# Runtime: 113 ms

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        if len(nums) == 2:
            return nums if nums[0] != nums[1] else [nums[0]]

        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        vals = [x for x in hashMap.items()]
        if len(vals) == 1:
            return [vals[0][0]]
        max1 = int(vals[0][1] < vals[1][1])
        max2 = 1 - max1
        for i in range(2, len(vals)):
            curr = vals[i][1]
            if curr > vals[max1][1]:
                max2 = max1
                max1 = i
            elif curr > vals[max2][1]:
                max2 = i
        
        requiredSize = len(nums) // 3
        print(vals)
        print(requiredSize)
        if vals[max2][1] > requiredSize:
            return [vals[max1][0], vals[max2][0]]
        if vals[max1][1] > requiredSize:
            return [vals[max1][0]]
        return []