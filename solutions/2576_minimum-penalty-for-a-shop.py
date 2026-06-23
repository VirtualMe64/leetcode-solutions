# Problem: https://leetcode.com/problems/minimum-penalty-for-a-shop
# Runtime: 66 ms

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        totalYs = customers.count('Y')
        ys = 0
        ns = 0
    
        minIdx = None
        minCost = None
        for i in range(len(customers)):
            cost = ns + totalYs - ys
            if minCost is None or cost < minCost:
                minCost = cost
                minIdx = i

            if customers[i] == 'Y':
                ys += 1
            else:
                ns += 1
    
        if ns < minCost:
            return len(customers)
        
        return minIdx