# Problem: https://leetcode.com/problems/permutations-ii
# Runtime: 55 ms

class Solution:
    def selectSpots(self, n, r):
        # return combinations to pick r spots from n possible
        curr = [[i] for i in range(n - r + 1)]
        for iteration in range(r - 1):
            new = []
            for combo in curr:
                for rem in range(combo[-1] + 1, n - r + iteration + 2):
                    new.append(combo + [rem])
            curr = new
        return curr

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        spots = len(nums)
        perms = [[None for _ in range(spots)]]
        for num, freq in freqs.items():
            newPerms = []
            for perm in perms:
                for spot in self.selectSpots(spots, freq):
                    newPerm = [x for x in perm]
                    nones = -1
                    spotIdx = 0
                    for i, v in enumerate(newPerm):
                        if v is None:
                            nones += 1
                        if spot[spotIdx] == nones:
                            newPerm[i] = num
                            spotIdx += 1
                            if spotIdx + 1 > freq:
                                break
                    newPerms.append(newPerm)
            
            perms = newPerms
            spots -= freq

        return perms