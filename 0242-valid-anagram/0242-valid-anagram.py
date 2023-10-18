class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s1_dict = {}
        s2_dict = {}
        
        for c in s:
            if c in s1_dict:
                s1_dict[c] += 1
            else:
                s1_dict[c] = 0
        
        for c in t:
            if c in s2_dict:
                s2_dict[c] += 1
            else:
                s2_dict[c] = 0
    
        for c in s1_dict:
            if c not in s2_dict or s1_dict[c] != s2_dict[c]:
                return False
        
        return True
        
        