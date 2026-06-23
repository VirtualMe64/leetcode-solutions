# Problem: https://leetcode.com/problems/zigzag-conversion
# Runtime: 15 ms

# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
    return s if num_rows == 1
    # add to output one row at a time
    out = ""
    num_rows.times do |row|
        curr = row # start idx
        # if first or last, delta is 2 * (num_rows - 1)
        # otherwise, deltas are:
        # 1. 2 * (num_rows - row - 1)
        # 2. 2 * row
        special = row == 0 || row == num_rows - 1
        deltas = special ? [2 * (num_rows - 1)] : [2 * (num_rows - row - 1), 2 * row]
        delta_idx = 0
        until curr >= s.size()
            # puts("#{s}, #{curr}, #{s[curr]}, #{out}")
            out << s[curr]
            curr += deltas[delta_idx]
            delta_idx += 1
            delta_idx %= deltas.size
        end
    end 
    out
end