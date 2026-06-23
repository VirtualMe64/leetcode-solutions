# Problem: https://leetcode.com/problems/roman-to-integer
# Runtime: 3 ms

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}



class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        last = 0

        for c in s:
            v = values[c]
            if v > last and last != 0: # subtraction
                total += v - last
                last = 0
            else:
                total += last
                last = v
        
        total += last
    
        return total