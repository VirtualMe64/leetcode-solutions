# Problem: https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i
# Runtime: 13721 ms

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        validPrefixes = set()
        
        for w in words:
            for i in range(len(w)):
                validPrefixes.add(w[0:i + 1])
    
        # now do dp
        # dp[i] is minimum number of substrs to get target[:i]
        dp = [None for i in range(len(target))] + [None]
        dp[0] = 0
        for i in range(len(target)):
            curr = dp[i]
            if curr is None:
                continue
            if dp[-1] is not None and curr + 1 >= dp[-1]:
                continue
            for l in range(1, len(target) - i + 1):
                substr = target[i : i + l]
                if substr in validPrefixes:
                    dp[i + l] = dp[i + l] if dp[i + l] is not None and dp[i + l] < curr + 1 else curr + 1
                else:
                    break
                
        return dp[-1] if dp[-1] is not None else -1