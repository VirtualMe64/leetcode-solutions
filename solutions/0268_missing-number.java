// Problem: https://leetcode.com/problems/missing-number
// Runtime: 0 ms

class Solution {
    public int missingNumber(int[] nums) {
        int totTrue = 0;
        int tot = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            totTrue += i;
            tot += nums[i];
        }
        return n + totTrue - tot;
    }
}