# Problem: https://leetcode.com/problems/apple-redistribution-into-boxes
# Runtime: 0 ms

# @param {Integer[]} apple
# @param {Integer[]} capacity
# @return {Integer}
def minimum_boxes(apple, capacity)
    sorted_capacity = capacity.sort.reverse
    idx = 0
    curr = apple.sum
    while curr > 0 do
        curr -= sorted_capacity[idx]
        idx += 1
    end
    return idx
end