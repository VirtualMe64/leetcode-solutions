// Problem: https://leetcode.com/problems/minimum-increment-to-make-array-unique
// Runtime: 12 ms

class Solution {
    private int MAX_NUM = 100000;

    public int minIncrementForUnique(int[] nums) {
        int[] numCount = new int[MAX_NUM + 1];
        for (Integer i : nums) {
            numCount[i] += 1;
        }
        int moves = 0;
        int carrying = 0;
        int seen = nums.length;
        for (Integer count : numCount) {
            moves += carrying;
            if (count == 0 && carrying > 0) {
                carrying -= 1;
            }
            if (count > 1) {
                carrying += count - 1;
            }
            seen -= count;
            if (seen <= 0) {
                break;
            }
        }
        moves += (carrying * (carrying + 1)) / 2;
        return moves;
    }
}