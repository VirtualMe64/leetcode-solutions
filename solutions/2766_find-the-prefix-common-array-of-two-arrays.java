// Problem: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays
// Runtime: 1 ms

class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        boolean[] seen = new boolean[A.length];
        int[] out = new int[A.length];
        int n = 0;

        for (int i = 0; i < A.length; i++) {
            if (seen[A[i] - 1])
                n += 1;
            seen[A[i] - 1] = true;

            if (seen[B[i] - 1])
                n += 1;
            seen[B[i] - 1] = true;

            out[i] = n;
        }

        return out;
    }
}