// Problem: https://leetcode.com/problems/delete-characters-to-make-fancy-string
// Runtime: 28 ms

class Solution {
    public String makeFancyString(String s) {
        StringBuilder out = new StringBuilder("");
        char last = '_';
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == last) {
                count += 1;
            } else {
                count = 1;
            }
            if (count < 3) {
                out.append(c);
            }
            last = c;
        }
        return out.toString();
    }
}