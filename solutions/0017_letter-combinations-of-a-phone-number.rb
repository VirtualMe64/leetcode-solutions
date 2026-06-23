# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number
# Runtime: 0 ms

def digit_to_letters(digit)
    val = digit.ord - '2'.ord
    offset = 3 * val
    offset += 1 if digit > '7'
    cnt = digit == '9' || digit == '7' ? 4 : 3
    return (offset...offset+cnt).map {|n| ('a'.ord + n).chr}
end

# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
    return [] if digits.length == 0
    return digit_to_letters(digits) if digits.length == 1
    suffixes = letter_combinations(digits[1..-1])
    out = []
    digit_to_letters(digits[0]).each do |c|
        suffixes.each do |suf|
            out << c + suf
        end
    end
    return out
end