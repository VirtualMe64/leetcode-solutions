# Problem: https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up
# Runtime: 586 ms

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        best = -1
        occurences = {}
        for i, card in enumerate(cards):
            if card in occurences:
                numCards = i - occurences[card] + 1
                best = min(best, numCards) if best != -1 else numCards
            occurences[card] = i
        return best