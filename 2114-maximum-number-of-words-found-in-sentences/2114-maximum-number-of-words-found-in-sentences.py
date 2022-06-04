class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_counter = 0
        
        for s in sentences:
            max_counter = max(max_counter, len(s.split()))
            
        return max_counter