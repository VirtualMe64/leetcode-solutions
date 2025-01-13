# Problem: https://leetcode.com/problems/total-appeal-of-a-string
# Runtime: 117 ms

class Solution:
    def appealSum(self, s: str) -> int:
        totalappeal = 0
        last_occurence_table = {}
        lastvalue = 0
        for i, c in enumerate(s):
            lastseen = last_occurence_table.get(c, -1)
            
            dist = i - lastseen
            
            newappeal = lastvalue
            newappeal += dist

            lastvalue = newappeal
            totalappeal += newappeal
            last_occurence_table[c] = i
        
        return totalappeal
    # abbca
    # a -> 1
    # b -> 3
    # b -> 4
    # c -> 8
    # a -> 13