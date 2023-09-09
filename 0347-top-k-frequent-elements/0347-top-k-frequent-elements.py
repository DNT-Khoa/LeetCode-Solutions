from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        bucket = [[] for i in range(len(nums) + 1)] 
        
        for num in count:
            freq = count[num]
            bucket[freq].append(num)
            
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for y in bucket[i]:
                res.append(y)
                if len(res) == k:
                    return res
        