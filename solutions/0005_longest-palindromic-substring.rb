# Problem: https://leetcode.com/problems/longest-palindromic-substring
# Runtime: 586 ms

# @param {String} s
# @return {String}
def longest_palindrome(s)
    return "" if s.length == 0
    longest = 1
    indices = [0, 0]
    # first, check all possible centers of odd length palindromes 
    1.upto(s.length - 1) do |ctr|
        l = ctr - 1
        r = ctr + 1
        until l < 0 or r >= s.length()
            break if s[l] != s[r]
            if r - l + 1 > longest
                longest = r - l + 1
                indices = [l, r]
            end
            l -= 1
            r += 1
        end
    end
    # next, check odd length palindromes
    0.upto(s.length - 2) do |ctr| # center is after s[ctr]
        l = ctr + 1
        r = ctr
        until l < 0 or r >= s.length()
            break if s[l] != s[r]
            if r - l + 1 > longest
                longest = r - l + 1
                indices = [l, r]
            end
            l -= 1
            r += 1
        end
    end
    return s[indices[0]..indices[1]]
end