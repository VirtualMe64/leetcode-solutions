# Problem: https://leetcode.com/problems/binary-prefix-divisible-by-5
# Runtime: 103 ms

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        val = 0
        for n in nums:
            val *= 2
            val += n
            answer.append(val % 5 == 0)
        return answer