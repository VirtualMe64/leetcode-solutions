// Problem: https://leetcode.com/problems/count-numbers-with-unique-digits
// Runtime: 0 ms

class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        int total = 1; // for 0
        for (int i = 1; i <= n; i++) {
            // i is length
            int curr = 9;
            for (int j = 1 ; j < i; j++) {
                curr *= 10 - j;
            }
            total += curr;
        }
        return total;
    }
}