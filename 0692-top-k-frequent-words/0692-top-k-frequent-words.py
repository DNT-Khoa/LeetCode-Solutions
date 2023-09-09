from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Group each word with their frequency
        count = Counter(words) # O(n)
        
        # Create a heap and initialize with count
        my_heap = [(-value, key) for key, value in count.items()] # O(n)
        heapq.heapify(my_heap)
        
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(my_heap)[1])
            
        return res
    