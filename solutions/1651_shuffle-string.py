# Problem: https://leetcode.com/problems/shuffle-string
# Runtime: 52 ms

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=[0]*len(indices)
        j=0
        for i in indices:
            x[i]=s[j]
            # print(i,x[i],j,s[j])
            j+=1
        return "".join(x)