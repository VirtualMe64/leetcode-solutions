// Problem: https://leetcode.com/problems/plus-one

class Solution {
    public int[] plusOne(int[] digits) {
        int idx = digits.length - 1;
        while (idx >= 0) {
            int val = digits[idx];
            if (val == 9) {
                digits[idx] = 0;
            } else {
                digits[idx] = val + 1;
                return digits;
            }
            idx--;
        }
        int[] newArr = new int[digits.length + 1];
        newArr[0] = 1;
        System.arraycopy(digits, 0, newArr, 1, digits.length);
        return newArr;
    }
}