// Problem: https://leetcode.com/problems/next-permutation
// Runtime: 5 ms

void swap(int* nums, int idx1, int idx2) {
    int temp = nums[idx1];
    nums[idx1] = nums[idx2];
    nums[idx2] = temp;
}

void reverse(int* nums, int startIndex, int numsSize) {
    for (int i = 0; i < (numsSize - startIndex) / 2; i++) {
        swap(nums, startIndex + i, numsSize - i - 1);
    }
}

void nextPermutation(int* nums, int numsSize) {
    if (numsSize <= 1) {
        return;
    }
    
    int breakpoint = -1;
    for (int i = numsSize - 2; i >= 0; i--) {
        if (nums[i] < nums[i + 1]) {
            breakpoint = i;
            break;
        }
    }
    
    if (breakpoint == -1) {
        reverse(nums, 0, numsSize);
        return;
    }
    for (int i = numsSize - 1; i > breakpoint; i--) {
        if (nums[i] > nums[breakpoint]) {
            swap(nums, i, breakpoint);
            reverse(nums, breakpoint + 1, numsSize);
            return;
        }
    }
}