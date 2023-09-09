import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        res = []
            
        # O(n)
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 0
            
        # Convert dictionary to heap => O(n)
        my_heap = [(-value, key) for key, value in my_dict.items()]
        heapq.heapify(my_heap)
        
        # Each pop in heap takes logn and we loop k times => O(k * logn)
        for i in range(k):
            res.append(heapq.heappop(my_heap)[1])
            
        return res
        
        ### Time complexity: O(nlogn)