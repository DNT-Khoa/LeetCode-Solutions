from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        
        for c in s:
            s1_dict[c] += 1
        
        for c in t:
            s2_dict[c] += 1
    
        for c in s1_dict:
            if c not in s2_dict or s1_dict[c] != s2_dict[c]:
                return False
        
        return True
        
        