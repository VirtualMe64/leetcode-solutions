// Problem: https://leetcode.com/problems/find-if-digit-game-can-be-won
// Runtime: 1 ms

class Solution {
    public boolean canAliceWin(int[] nums) {
        int singleSum = 0;
        int doubleSum = 0;
        for (Integer i : nums) {
            if (i >= 10) {
                doubleSum += i;
            } else {
                singleSum += i;
            }
        }
        return singleSum != doubleSum;
    }
}