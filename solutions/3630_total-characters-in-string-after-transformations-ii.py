# Problem: https://leetcode.com/problems/total-characters-in-string-after-transformations-ii
# Runtime: 1118 ms

import numpy as np

MOD = (10 ** 9) + 7

def matrix_pow(mat, power, modulus):
    if power == 0:
        return np.eye(mat.shape[0], dtype=object)
    if power == 1:
        return mat
    half_res = matrix_pow(mat, power // 2, modulus)
    if power % 2 == 0:
        return (half_res @ half_res) % modulus
    else:
        return (half_res @ half_res @ mat) % modulus

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # idea 1: matrix repr + naive multiplication
        # idea 2: smarter matrix multiplication
        mat = np.zeros((26, 26), dtype=object)
        for i in range(26):
            start = i + 1
            end = start + nums[i]
            overflow = max(end - 26, 0)

            mat[i, start:end] = 1
            mat[i, 0:overflow] = 1
        res = matrix_pow(mat, t, MOD)
        vec = np.zeros(26, dtype=object)
        for c in s:
            vec[ord(c) - ord('a')] += 1
        
        out = vec @ res
        return int(sum(out)) % MOD