# Problem: https://leetcode.com/problems/maximum-matching-of-players-with-trainers
# Runtime: 72 ms

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        idx1 = 0
        idx2 = 0
        while idx1 < len(players) and idx2 < len(trainers):
            if players[idx1] <= trainers[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                idx2 += 1

        return idx1