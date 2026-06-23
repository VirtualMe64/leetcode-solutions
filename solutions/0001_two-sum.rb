# Problem: https://leetcode.com/problems/two-sum
# Runtime: 0 ms

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    seen = {}
    nums.each_with_index do |elem, idx|
        needed = target - elem
        if seen.key?(needed)
            return [seen[needed], idx]
        end
        seen[elem] = idx
    end
    return false
end