# Problem: https://leetcode.com/problems/unique-paths
# Runtime: 28 ms

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # number of waits to array string of m D and n R
        # (m + n) choose m
        '''
        m = m - 1
        n = n - 1
        total = 1
        curr = m + n
        for i in range(min(m, n)):
            total *= curr
            curr -= 1
        for i in range(min(m, n)):
            total = total // (i + 1)
        return total
        '''
        return efficientChoose(m - 1 + n - 1, min(m - 1, n - 1))

def efficientChoose(n, k):
    if k == 0:
        return 1
    return (n * efficientChoose(n - 1, k - 1)) // k