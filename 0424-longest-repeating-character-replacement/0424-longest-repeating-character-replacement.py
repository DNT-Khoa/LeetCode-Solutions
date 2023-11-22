class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26 
        left = right = 0
        maxLength = 0
        
        while right < len(s):
            counter[ord(s[right]) - ord("A")] += 1
            currLength = right - left + 1
            maxFreq = max(counter)
            
            if currLength - maxFreq <= k:
                maxLength = max(maxLength, currLength)
            else:
                counter[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        
        return maxLength
        
        
        
        
        