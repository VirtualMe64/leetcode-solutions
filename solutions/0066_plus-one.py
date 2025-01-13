# Problem: https://leetcode.com/problems/plus-one
# Runtime: 16 ms

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1
        while idx > -1:
            val = digits[idx]
            if val == 9:
                digits[idx] = 0
                idx -= 1
            else:
                digits[idx] = val + 1
                return digits
        digits.insert(0, 1)
        return digits