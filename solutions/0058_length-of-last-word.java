// Problem: https://leetcode.com/problems/length-of-last-word
// Runtime: 0 ms

class Solution {
    public int lengthOfLastWord(String s) {
        int out = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') {
                if (out == 0) {
                    continue;
                }
                return out;
            }
            out++;
        }
        return out;
    }
}