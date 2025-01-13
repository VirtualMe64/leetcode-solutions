// Problem: https://leetcode.com/problems/ugly-number
// Runtime: 0 ms

import java.lang.Math;

class Solution {
    public boolean isUgly(int n) {
        if (n <= 0) {
            return false;
        }
        int curr = 2;
        while (curr <= 5) {
            if (n % curr == 0) {
                n = n / curr;
            } else {
                curr += 1;
            }
        }
        return n == 1;
    }
}