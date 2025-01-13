// Problem: https://leetcode.com/problems/compare-version-numbers
// Runtime: 1 ms

class Solution {
    public int compareVersion(String version1, String version2) {
        int ptr1 = 0;
        int ptr2 = 0;

        while (ptr1 < version1.length() || ptr2 < version2.length()) {
            StringBuilder val1 = new StringBuilder();
            StringBuilder val2 = new StringBuilder();

            while (ptr1 < version1.length() && version1.charAt(ptr1) != '.') {
                val1.append(version1.charAt(ptr1++));
            }
            while (ptr2 < version2.length() && version2.charAt(ptr2) != '.') {
                val2.append(version2.charAt(ptr2++));
            }

            ptr1++;
            ptr2++;

            int num1 = val1.length() == 0 ? 0 : Integer.parseInt(val1.toString());
            int num2 = val2.length() == 0 ? 0 : Integer.parseInt(val2.toString());
            if (num1 > num2) {
                return 1;
            }
            if (num2 > num1) {
                return -1;
            }
        }

        return 0;
    }
}