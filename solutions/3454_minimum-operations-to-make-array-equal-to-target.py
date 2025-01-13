# Problem: https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target
# Runtime: 755 ms

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        # idea 1: easier to work with list of differences
        # nums = [3,5,1,2], target = [4,6,2,4] => diffs = [1, 1, 1, 2]
        # nums = [1,3,2], target = [2,1,4] => diffs = [1, -2, 2]
        # idea 2: we want runs of the same sign, optimal solution is always doing best run
        # in something like [pos run, neg run, pos run], there's no advantage to doing whole thing
        # idea 3: moves needed for a run is the max of the run
        # idea 3 is wrong: [3, 2, 3] takes 4 moves, [1, 2, 1, 2] takes 3
        # idea 4: whenever we go down, that's free, but resets our max
        
        diffs = [target[i] - nums[i] for i in range(len(nums))]
        
        total = 0
        prevSign = 0
        prev = 0
        
        for diff in diffs:
            if diff > 0:
                if prevSign != 1:
                    total += diff
                elif diff > prev: # gotta increase
                    total += diff - prev
            elif diff < 0:
                if prevSign != -1:
                    total += -diff
                elif diff < prev: # gotta increase
                    total += prev - diff
                    
            prev = diff
            prevSign = 1 if diff > 0 else (-1 if diff < 0 else 0)
        
        return total