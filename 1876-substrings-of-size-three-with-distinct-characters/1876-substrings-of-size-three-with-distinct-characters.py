class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        counter = 0
        
        i = 0
        while i+2 < len(s):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
                counter+=1
            i+=1
        
        return counter