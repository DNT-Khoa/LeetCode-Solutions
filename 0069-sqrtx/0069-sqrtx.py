class Solution:
    def mySqrt(self, x: int) -> int:
        def isValid(n):
            return n*n > x
        
        l, r = 0, x + 1
        while l < r:
            m = l + (r - l) // 2
            if isValid(m):
                r = m
            else:
                l = m + 1
        
        return l - 1