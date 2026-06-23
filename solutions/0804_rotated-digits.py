# Problem: https://leetcode.com/problems/rotated-digits
# Runtime: 26 ms

class Solution:
    def rotatedDigits(self, n: int) -> int:
        def check(k):
            change = False
            while k > 0:
                digit = k % 10

                if digit in [0, 1, 8]:
                    pass
                elif digit in [2, 5, 6, 9]:
                    change = True
                else:
                    return False
                
                k //= 10
        
            return change

        count = 0
        for i in range(1, n + 1):
            if check(i):
                count += 1
        return count