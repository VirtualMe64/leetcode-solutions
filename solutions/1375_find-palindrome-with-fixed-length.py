# Problem: https://leetcode.com/problems/find-palindrome-with-fixed-length
# Runtime: 75 ms

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        cache = {}
        # if intLength is even this is easy -- ith palindrome is ith number
        # of length intLength // 2 without leading 0s palindromed
        # odd is same concept but intLength // 2 + 1
        even = intLength % 2 == 0
        palLength = intLength // 2 if even else (intLength // 2) + 1
        start = 10 ** (palLength - 1) # i.e for length = 3, start is 100
        numPals = (10 ** palLength) - start # i.e all between 100 and 999

        out = []
        for q in queries:
            if q in cache:
                out.append(cache[q])
                continue
            if q > numPals:
                out.append(-1)
                continue
            base = str(start + (q - 1))
            if even:
                rev = base[::-1] # i.e 100 -> 001
            else:
                rev = base[::-1][1:] # i.e 100 -> 01 (since odd)
            res = int(base + rev)
            out.append(res)
            cache[q] = res
        return out            