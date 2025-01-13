# Problem: https://leetcode.com/problems/merge-sorted-array
# Runtime: 47 ms

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = 0
        ptr2 = 0

        moved = 0

        while ptr2 < n:
            if (ptr1 - moved) >= m or nums1[ptr1] > nums2[ptr2]:
                nums1.insert(ptr1, nums2[ptr2])
                ptr2 += 1
                moved += 1
            ptr1 += 1

        del nums1[m + n:]