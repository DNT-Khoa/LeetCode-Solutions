class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def possible(waitDays):
            flowers = 0
            bouquets = 0
            
            for f in bloomDay:
                if f > waitDays:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            
            return bouquets >= m
        
        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
                    