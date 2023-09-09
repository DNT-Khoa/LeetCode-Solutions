import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert the list into a heap
        my_heap = [-n for n in nums]
        heapq.heapify(my_heap)
        
        for i in range(k):
            value = heapq.heappop(my_heap)
            if i == k - 1:
                return -value
            
        return 0