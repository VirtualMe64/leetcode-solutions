# Problem: https://leetcode.com/problems/decode-the-slanted-ciphertext
# Runtime: 247 ms

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        out = ""
        for row in range(cols):
            x = row
            y = 0
            
            while x < cols and y < rows:
                v = encodedText[y * cols + x]
                out += v
                
                x += 1
                y += 1

        return out.rstrip()