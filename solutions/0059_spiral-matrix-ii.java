// Problem: https://leetcode.com/problems/spiral-matrix-ii
// Runtime: 0 ms

class Solution {
    public int[][] generateMatrix(int n) {
        int[][] out = new int[n][n];

        int x = 0;
        int y = 0;
        int dx = 1;
        int dy = 0;

        int xMin = 0;
        int yMin = 0;
        int xMax = n - 1;
        int yMax = n - 1;

        for (int i = 1; i <= n * n; i++) {
            // System.out.format("x: %d, y: %d, dx: %d, dy: %d,. i: %d\n", x, y, dx, dy, i);
            out[y][x] = i;
            x += dx;
            y += dy;

            if ((dx == 1 && x >= xMax) || (dx == -1 && x <= xMin)) {
                if (dx == 1) {
                    yMin += 1;
                } else {
                    yMax -= 1;
                }
                dy = dx;
                dx = 0;
                continue;
            }
            
            if ((dy == 1 && y >= yMax) || (dy == -1 && y <= yMin)) {
                if (dy == 1) {
                    xMax -= 1;
                } else {
                    xMin += 1;
                }
                dx = -dy;
                dy = 0;
                continue;
            }
        }

        return out;
    }
}