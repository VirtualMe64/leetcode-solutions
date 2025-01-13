// Problem: https://leetcode.com/problems/string-compression-iii
// Runtime: 23 ms

class Solution {
    public String compressedString(String word) {
        StringBuilder comp = new StringBuilder("");

        char last = '_';
        int count = 0;

        for (char c : word.toCharArray()) {
            if (c == last) {
                count += 1;
                if (count == 9) {
                    comp.append(String.valueOf(count));
                    comp.append(last);
                    count = 0;
                }
            } else if (count > 0) {
                comp.append(String.valueOf(count));
                comp.append(last);
                last = c;
                count = 1;
            } else {
                last = c;
                count = 1;
            }
        }

        if (count > 0) {
            comp.append(String.valueOf(count));
            comp.append(last);
        }

        return comp.toString();
    }
}