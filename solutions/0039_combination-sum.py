# Problem: https://leetcode.com/problems/combination-sum
# Runtime: 23 ms

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSumRec(candidates, 0, target)
    
    def combinationSumRec(self, sortedCandidates, start, target):
        if start >= len(sortedCandidates):
            return []

        curr = [start, 0] # current index and count

        out = []

        while curr[0] < len(sortedCandidates):
            curr[1] += 1
            base = [sortedCandidates[curr[0]]] * curr[1]

            cost = sortedCandidates[curr[0]] * curr[1]
            rem = target - cost
            if rem == 0:
                out.append(base.copy())
            elif rem < 0:
                curr = [curr[0] + 1, 0]
            else:
                additions = self.combinationSumRec(sortedCandidates, curr[0] + 1, rem)
                for a in additions:
                    out.append(base.copy() + a)

        return out