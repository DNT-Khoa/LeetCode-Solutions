class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = right = maxLength = 0
        
        while right < len(s):
            if s[right] in visited:
                while s[left] != s[right]:
                    visited.remove(s[left])
                    left += 1
                left += 1
            
            newLength = right - left + 1
            maxLength = max(maxLength, newLength)
            visited.add(s[right])
            right += 1
                
        return maxLength
        
        
        