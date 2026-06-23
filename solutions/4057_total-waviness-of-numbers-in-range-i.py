# Problem: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i
# Runtime: 427 ms

class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def waviness(n):
            total = 0
            nStr = str(n)
            for i in range(1, len(nStr) - 1):
                v1, v2, v3 = nStr[i - 1], nStr[i], nStr[i + 1]
                if v1 < v2 and v2 > v3:
                    total += 1
                elif v1 > v2 and v2 < v3:
                    total += 1
            return total

        return sum(waviness(i) for i in range(num1, num2 + 1))