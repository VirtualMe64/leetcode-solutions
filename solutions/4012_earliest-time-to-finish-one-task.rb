# Problem: https://leetcode.com/problems/earliest-time-to-finish-one-task
# Runtime: 1 ms

# @param {Integer[][]} tasks
# @return {Integer}
def earliest_time(tasks)
    tasks.map { |t| t[0] + t[1] }.min
end