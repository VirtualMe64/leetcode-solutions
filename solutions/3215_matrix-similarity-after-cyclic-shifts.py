# Problem: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts
# Runtime: 0 ms

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                otherIdx = ((j + k) if i % 2 == 0 else (j - k)) % len(row)
                if v != row[otherIdx]:
                    return False
        
        return True