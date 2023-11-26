class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def possible(waitDays):
            l = -1
            maxBouquet = 0
            
            for r in range(len(bloomDay)):
                if bloomDay[r] <= waitDays:
                    d = r - l
                    if d == k:
                        maxBouquet += 1
                        l = r
                else:
                    l = r
            
            return maxBouquet >= m
        
        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
                    