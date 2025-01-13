// Problem: https://leetcode.com/problems/majority-element-ii
// Runtime: 19 ms

import java.util.ArrayList;
import java.util.HashSet;


class Solution {
    public List<Integer> majorityElement(int[] nums) {
        return new ArrayList<Integer>(majorityHelper(nums, 0, nums.length));
    }

    // returns, if it exists, all 1/3 majority element
    // start: inclusive, end: exclusive
    public Set<Integer> majorityHelper(int[] nums, int start, int end) {
        Set<Integer> out = new HashSet<>();
        int len = end - start;
        if (len < 3) { // base case: for len 0, 1, 2, include all
            for (int i = start; i < end; i++) {
                out.add(nums[i]);
            }
            return out;
        }
        // otherwise, split into 3 and recurse
        // 1 -> 1, 2 -> 1, 3 -> 1, 4 -> 2 -- ceil(n / 3)
        int partition = (len + 2) / 3;
        Set<Integer> l1 = majorityHelper(nums, start, start + partition);
        Set<Integer> l2 = majorityHelper(nums, start + partition, start + 2 * partition);
        Set<Integer> l3 = majorityHelper(nums, start + 2 * partition,
                                            Math.min(end, start + 3 * partition));
        for (Integer i : checkMajority(l1, nums, start, end)) {
            out.add(i);
        }
        for (Integer i : checkMajority(l2, nums, start, end)) {
            out.add(i);
        }
        for (Integer i : checkMajority(l3, nums, start, end)) {
            out.add(i);
        }
        return out;
    }

    public Set<Integer> checkMajority(Set<Integer> options, int[] nums, int start, int end) {
        int rec = (end - start) / 3; // minimum to be considered majority
        Set<Integer> out = new HashSet<>();
        for (Integer o : options) {
            int count = 0;
            for (int i = start; i < end; i++) {
                if (nums[i] == o) {
                    count++;
                }
            }
            if (count > rec) {
                out.add(o);
            }
        }
        return out;
    }
}