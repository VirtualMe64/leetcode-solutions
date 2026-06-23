# Problem: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i
# Runtime: 32 ms

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # two options:
        # 1. sequence of same parity (i.e 1 1 1 1 1)
        # 2. sequence of alternating parity (i.e 1 0 1 0)

        same_parity_0_cnt = 0
        same_parity_1_cnt = 0
        alternating_parity_cnt = 0
        last_parity = None

        for n in nums:
            parity = n % 2

            if parity == 0:
                same_parity_0_cnt += 1
            else:
                same_parity_1_cnt += 1
            
            if parity != last_parity:
                alternating_parity_cnt += 1
                last_parity = parity

        return max(same_parity_0_cnt, same_parity_1_cnt, alternating_parity_cnt)