# Problem: https://leetcode.com/problems/string-to-integer-atoi
# Runtime: 4 ms

MIN_VAL= -2.pow(31)
MAX_VAL = 2.pow(31) - 1

# @param {String} s
# @return {Integer}
def my_atoi(s)
    idx = s.size - 1
    out = 0
    started = false
    pos = true
    s.each_char.with_index do |c, idx|
        val = c.ord - '0'.ord
        non_digit = (val < 0 || val >= 10) # anything other than 0-9
        if non_digit
            break if started # any non digit after we've started means we're done
            if c == '+' || c == '-' # we will accept one +/- to determine sign
                pos = c == '+'
                started = true
                next
            elsif c == ' ' # ignore leading whitespace
                next
            else
                break # any other character (i.e d), we break
            end
        end
        started = true
        out *= 10
        out += val
    end
    out = pos ? out : -out

    out = out < MIN_VAL ? MIN_VAL : out
    out = out > MAX_VAL ? MAX_VAL : out
    return out
end