# Problem: https://leetcode.com/problems/finding-3-digit-even-numbers
# Runtime: 3 ms

# @param {Integer[]} digits
# @return {Integer[]}
def find_even_numbers(digits)
    cnts = {}
    (0..9).each {|d| cnts[d] = 0}
    digits.each {|d| cnts[d] = cnts[d] + 1} 
    
    out = []
    cnts.each_pair do |first_digit, freq0|
        # no leading zeros
        next if first_digit.zero? || freq0 == 0
        
        # next select the first digit
        cnts.each_pair do |mid_digit, freq1|
            # invalid if count is 1 and already used
            uses = first_digit == mid_digit ? 1 : 0
            next if uses >= freq1

            # finally, select middle digit
            cnts.each_pair do |end_digit, freq2|
                # must be even, which depends on last digit
                next if end_digit % 2 != 0

                # also must appear enough times in array
                uses = 0
                uses += 1 if end_digit == first_digit
                uses += 1 if end_digit == mid_digit
                next if uses >= freq2

                # valid number, construct it!
                out << first_digit * 100 + mid_digit * 10 + end_digit
            end
        end
    end

    return out
end