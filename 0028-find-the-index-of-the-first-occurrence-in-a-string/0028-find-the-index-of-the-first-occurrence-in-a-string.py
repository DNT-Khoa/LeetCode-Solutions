class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hLen = len(haystack)
        nLen = len(needle)
        
        if nLen == 0:
            return 0
        
        if hLen < nLen:
            return -1
        
        for i in range(hLen):
            if haystack[i] == needle[0]:
                for j in range(nLen):
                    if i + j == hLen:
                        break
                    if haystack[i + j] != needle[j]:
                        break
                    if j == nLen - 1:
                        return i
        
        return -1
                    
                
                