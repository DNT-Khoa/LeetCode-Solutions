class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            curCap = 0
            curDays = 1
            
            for w in weights:
                curCap += w
                if curCap > capacity:
                    curDays += 1
                    curCap = w
                    
            return curDays <= days
        
        # Find 
        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            if possible(m):
                r = m
            else:
                l = m + 1
        
        return l
                
                
                    