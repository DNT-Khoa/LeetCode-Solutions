class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        newString = haystack.replace(needle, "K")
        for i in range(len(newString)):
            if newString[i] == "K":
                return i
        
        return -1