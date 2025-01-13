// Problem: https://leetcode.com/problems/rotate-image
// Runtime: 0 ms

class Solution {
    public void rotate(int[][] matrix) {
        int temp1, temp2;
        int len = matrix.length;
        for (int layer = 0; layer < len / 2; layer++) {
            for (int index = layer; index < len - layer - 1; index++) {
                temp2 = matrix[layer][index];
                temp1 = matrix[index][len - layer - 1];
                matrix[index][len - layer - 1] = temp2;

                temp2 = temp1;
                temp1 = matrix[len - layer - 1][len - index - 1];
                matrix[len - layer - 1][len - index - 1] = temp2;

                temp2 = temp1;
                temp1 = matrix[len - index - 1][layer];
                matrix[len - index - 1][layer] = temp2;

                matrix[layer][index] = temp1;
            }
        }
    }
}