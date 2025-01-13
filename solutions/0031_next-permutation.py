# Problem: https://leetcode.com/problems/next-permutation

def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1, 2, 3]
        [1, 3, 2]
        [2, 1, 3]
        [2, 3, 1]
        [3, 1, 2]
        [3, 2, 1]
        """
        if len(nums) <= 1:
            return
        if len(nums) == 2:
            swap(nums, 0, 1)
            return

        # step 1: identify smallest place value that can be improved
        ptr1 = len(nums) - 2
        largest = nums[ptr1 + 1]
        while nums[ptr1] >= largest:
            largest = nums[ptr1]
            ptr1 -= 1
        
        # step 2: find index to swap with
        smallestGap = None
        smallestGapIndex = len(nums) - 1
        for ptr2 in range(ptr1 + 1, len(nums)):
            diff = nums[ptr2] - nums[ptr1]
            if diff > 0:
                if smallestGap == None or diff < smallestGap:
                    smallestGap = diff
                    smallestGapIndex = ptr2
        ptr2 = smallestGapIndex

        print(ptr1, ptr2) 

        # step 3: shift ptr2 to ptr1, sorting as we go
        nums.insert(max(ptr1, 0), nums.pop(ptr2))
        nums[ptr1 + 1:] = sorted(nums[ptr1 + 1:])