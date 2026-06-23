# Problem: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i
# Runtime: 2 ms

# @param {String[]} words
# @param {Integer[]} groups
# @return {String[]}
def get_longest_subsequence(words, groups)
    out = []
    curr = nil
    words.zip(groups).each do |w, g| 
        if g != curr
            curr = g
            out << w
        end
    end
    return out
end