// Problem: https://leetcode.com/problems/remove-element
// Runtime: 0 ms

class Solution {
    public int removeElement(int[] nums, int val) {
        int ptr1 = 0; // next location to place elem
        int removed = 0;

        for (int ptr2 = 0; ptr2 < nums.length; ptr2++) {
            if (nums[ptr2] != val) {
                nums[ptr1] = nums[ptr2];
                ptr1++;
            }
        }

        return ptr1;
    }
}