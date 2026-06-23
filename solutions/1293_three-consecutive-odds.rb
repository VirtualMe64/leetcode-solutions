# Problem: https://leetcode.com/problems/three-consecutive-odds
# Runtime: 0 ms

# @param {Integer[]} arr
# @return {Boolean}
def three_consecutive_odds(arr)
    cnt = 0
    arr.each do |n| 
        n % 2 == 1 ? cnt += 1 : cnt = 0
        return true if cnt == 3 
    end
    result = false
end