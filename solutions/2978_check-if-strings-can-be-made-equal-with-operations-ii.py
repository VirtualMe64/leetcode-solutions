# Problem: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii
# Runtime: 160 ms

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        def getCnts(s):
            evenCnt = {}
            oddCnt = {}

            for i, c in enumerate(s):
                if i % 2 == 0: evenCnt[c] = evenCnt.get(c, 0) + 1
                else: oddCnt[c] = oddCnt.get(c, 0) + 1

            return evenCnt, oddCnt

        evenCnt1, oddCnt1 = getCnts(s1)
        evenCnt2, oddCnt2 = getCnts(s2)

        for c in evenCnt1.keys():
            if evenCnt1.get(c, 0) != evenCnt2.get(c, 0):
                return False
        
        for c in oddCnt1.keys():
            if oddCnt1.get(c, 0) != oddCnt2.get(c, 0):
                return False
        
        return True