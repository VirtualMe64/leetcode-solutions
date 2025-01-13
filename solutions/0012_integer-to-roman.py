# Problem: https://leetcode.com/problems/integer-to-roman
# Runtime: 42 ms

class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [('?', 'M', 1000), ('D', 'C', 100), ('L', 'X', 10), ('V', 'I', 1)]

        idx = 0
        out = ""

        while num > 0:
            curr_5_symbol, curr_1_symbol, curr_val = vals[idx]
            if curr_val > num:
                idx += 1
                continue
            
            n = num // curr_val
            num -= n * curr_val
            if n == 9:
                out += (curr_1_symbol + vals[idx - 1][1])
            elif n > 5:
                out += (curr_5_symbol + (n - 5) * curr_1_symbol)
            elif n == 5:
                out += (curr_5_symbol)
            elif n == 4:
                out += (curr_1_symbol + curr_5_symbol)
            elif n > 0:
                out += (n * curr_1_symbol)
            else:
                continue
 
        return out