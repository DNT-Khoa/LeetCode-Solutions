class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        counter = 0
        
        p1 = 0
        p2 = 1
        p3 = 2
        
        while p3 < len(s):
            if s[p1] != s[p2] and s[p2] != s[p3] and s[p1] != s[p3]:
                counter += 1
            p1 += 1
            p2 += 1
            p3 += 1
        
        return counter