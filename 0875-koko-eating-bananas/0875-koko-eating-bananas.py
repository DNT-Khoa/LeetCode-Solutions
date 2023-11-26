import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p / k)
            return totalHours <= h
        
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            
            if possible(m):
                r = m
            else:
                l = m + 1
        
        return l