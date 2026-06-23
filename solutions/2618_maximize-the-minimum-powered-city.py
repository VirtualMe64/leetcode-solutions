# Problem: https://leetcode.com/problems/maximize-the-minimum-powered-city
# Runtime: 1143 ms

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        cities = []

        currSum = sum(stations[:r + 1])
        for i in range(len(stations)):
            cities.append(currSum)

            left = i - r
            right = i + r + 1

            if left >= 0:
                currSum -= stations[left]

            if right < len(stations):
                currSum += stations[right]

        def isPossible(minPower):
            # checks if we can achieve a minimum power of minPower for all cities

            cost = 0
            currPower = 0
            dropoffs = {}
            for i in range(len(cities)):
                required = minPower - cities[i]
                currPower -= dropoffs.get(i, 0)

                if currPower >= required:
                    continue
                
                delta = required - currPower
                cost += delta
                currPower += delta
                dropoffs[i + 2 * r + 1] = delta
            
                if cost > k:
                    return False
            
            return True
        
        lower = 0 # inclusive
        upper = min(cities) + k # inclusive

        while upper > lower:
            middle = (upper + lower + 1) // 2
            if isPossible(middle):
                lower = middle
            else:
                upper = middle - 1
        
        return upper