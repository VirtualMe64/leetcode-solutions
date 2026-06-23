# Problem: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid
# Runtime: 853 ms

class Solution:
    def buildDiags(self, grid):
        m = len(grid)
        n = len(grid[0])
        diagSums = []

        for i in range(m):
            cumSum = [0]
            curr = 0
            for j in range(i + 1):
                if j >= n:
                    break
                curr += grid[i - j][j]
                cumSum.append(curr)
            diagSums.append(cumSum)
        
        newSums = []
        for i in range(n - 1):
            cumSum = [0]
            curr = 0
            for j in range(i + 1):
                if m - j - 1 < 0:
                    break
                curr += grid[m - j - 1][n - i + j - 1]
                cumSum.append(curr)
            newSums.append(cumSum)
        diagSums.extend(newSums[::-1])

        return diagSums

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        upRightSums = self.buildDiags(grid)

        revGrid = [row[::-1] for row in grid]
        upLeftSums = self.buildDiags(revGrid)

        top3 = []

        def addVal(v):
            if v in top3:
                return
            if len(top3) < 3:
                top3.append(v)
            elif v > top3[-1]:
                top3.pop(-1)
                top3.append(v)
            top3.sort(reverse=True)

        def oob(y, x):
            if x < 0 or x >= n or y < 0 or y >= m:
                return True
            return False

        for topY in range(m):
            for topX in range(n):
                addVal(grid[topY][topX])
                for sl in range(1, min(m, n)): # sidelength
                    up = (topY, topX)
                    left = (topY + sl, topX - sl)
                    right = (topY + sl, topX + sl)
                    bot = (topY + (sl * 2), topX)

                    if oob(*up) or oob(*left) or oob(*right) or oob(*bot):
                        break
                    
                    ulBase = upRightSums[up[0] + up[1]]
                    ulIdx1 = min(m - left[0], left[1] + 1)
                    ulIdx2 = min(m - up[0], up[1] + 1)
                    ulVal = ulBase[ulIdx2] - ulBase[ulIdx1 - 1]

                    brBase = upRightSums[right[0] + right[1]]
                    brIdx1 = min(m - bot[0], bot[1] + 1)
                    brIdx2 = min(m - right[0], right[1] + 1)
                    brVal = brBase[brIdx2] - brBase[brIdx1 - 1]

                    urBase = upLeftSums[up[0] + (n - up[1] - 1)]
                    urIdx1 = min(m - right[0], n - right[1])
                    urIdx2 = min(m - up[0], n - up[1])
                    urVal = urBase[urIdx2] - urBase[urIdx1 - 1]
                    
                    blBase = upLeftSums[left[0] + (n - left[1] - 1)]
                    blIdx1 = min(m - bot[0], n - bot[1])
                    blIdx2 = min(m - left[0], n - left[1])
                    blVal = blBase[blIdx2] - blBase[blIdx1 - 1]

                    rhombusSum = ulVal + urVal + brVal + blVal
                    # remove double counted corners
                    for c in [up, right, bot, left]:
                        rhombusSum -= grid[c[0]][c[1]]

                    addVal(rhombusSum)

        return top3