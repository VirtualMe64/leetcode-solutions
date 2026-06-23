# Problem: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings
# Runtime: 311 ms

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # variant of LCS
        # optimization: circular dp array (insted of table or swapping two arrays)
        max_val = (len(s1) + len(s2)) * ord('z')
        dp_table = [max_val for i in range(len(s1) + 1)]
        prev = None

        for j in range(len(s2) + 1):
            for i in range(len(s1) + 1):
                if i == 0 and j == 0:
                    dp_table[0] = 0
                    continue

                left_option = dp_table[i - 1] + ord(s1[i - 1]) if i > 0 else max_val
                up_option = dp_table[i] + ord(s2[j - 1]) if j > 0 else max_val
                
                matched_option = max_val
                if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
                    matched_option = prev

                prev = dp_table[i]
                dp_table[i] = min(left_option, up_option, matched_option)

            # print(dp_table)

        return dp_table[-1]