# Problem: https://leetcode.com/problems/candy
# Runtime: 126 ms

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        # first pass: forward
        prevRating = -1
        prevCandies = 0
        for i, rating in enumerate(ratings):
            if rating > prevRating:
                candies[i] = prevCandies + 1
            prevRating = rating
            prevCandies = candies[i]
        
        print(candies)

        prevRating = -1
        prevCandies = 0
        # second pass: backwards
        for i in range(len(ratings)):
            idx = len(ratings) - i - 1
            rating = ratings[idx]
            if rating > prevRating:
                minCandies = prevCandies + 1
                candies[idx] = max(candies[idx], minCandies)
            prevRating = rating
            prevCandies = candies[idx]
    
        # third pass: sum
        total = 0
        for candy in candies:
            total += candy

        return total