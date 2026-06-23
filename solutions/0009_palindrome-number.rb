# Problem: https://leetcode.com/problems/palindrome-number
# Runtime: 0 ms

# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    s = x.to_s
    s.reverse == s
    # return false if x < 0

    # oldReversed = nil
    # orig = x
    # reversed = 0
    # while x > 0
    #     reversed = (reversed * 10) + (x % 10)
    #     x /= 10
    # end
    # return reversed == orig
end