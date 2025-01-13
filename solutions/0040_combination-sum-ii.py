# Problem: https://leetcode.com/problems/combination-sum-ii
# Runtime: 154 ms

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ways = {}

        for num in candidates:
            items = [x for x in ways.items()]
            for way, combos in items:
                if way > target:
                    continue
                for combo in combos:
                    val = way + num
                    curr = ways.get(val, [])
                    new = sorted(combo + [num])
                    if new not in curr:
                        ways[val] = curr + [new]

            curr = ways.get(num, [])
            if [num] not in curr:
                curr += [[num]]
                ways[num] = curr

        return ways.get(target, [])