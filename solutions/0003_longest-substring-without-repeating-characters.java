// Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
    HashMap<Character, Integer> lookUpTable = new HashMap<>(); 

    public int lengthOfLongestSubstring(String s) {
        int length = 0;
        int longest = 0;
        for (int i = 0; i < s.length(); i++) {
            int lastOcc = lookUpTable.getOrDefault(s.charAt(i), -1);
            lookUpTable.put(s.charAt(i), i);
            if (i - lastOcc > length) {
                // this char won't be duplicate
                length += 1;
                longest = length > longest ? length : longest; // max
            } else {
                length = i - lastOcc;
            }
        }

        return longest;
    }
}