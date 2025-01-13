// Problem: https://leetcode.com/problems/two-sum
// Runtime: 7 ms

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            int needed = target - curr;
            if (dict.containsKey(needed)) {
                return new int[] {i, dict.get(needed)};
            }
            dict.put(curr, i);
        }
        return null;
    }
}