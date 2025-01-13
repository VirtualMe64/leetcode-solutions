# Problem: https://leetcode.com/problems/generate-parentheses
# Runtime: 12 ms

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        dp plan: table with t(i, j) = number of ways to get balance factor of j with i characters
        note that if balance is ever negative, solution is invalid so value is 0
        t(i, j) = t(i - 1, j - 1) + t(i - 1, j + 1)
        """
        k = 2 * n + 1
        dp_table = [[[] for _ in range(k)] for _ in range(k)]
        dp_table[0][0] = [""]
        getVal = lambda i, j : dp_table[i][j] if i >= 0 and j >= 0 and j < k and i < k else []
        
        for i in range(1, k):
            for j in range(k):
                options1 = [x + "(" for x in getVal(j - 1, i - 1)]
                options2 = [x + ")" for x in getVal(j + 1, i - 1)]
                dp_table[j][i] = options1 + options2

        return dp_table[0][k-1]