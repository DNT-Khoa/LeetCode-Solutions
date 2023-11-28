from heapq import *
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        n = len(arr)
        bucket = [[] for _ in range(n + 1)]
        
        for num, occurence in cnt.items():
            bucket[occurence].append(num)
        
        for b in range(len(bucket)):
            if bucket[b]:
                total = b * len(bucket[b])
                
                if k > total:
                    k -= total
                    bucket[b].clear()
                elif k <= total:
                    numOfPops = k // b
                    for _ in range(numOfPops):
                        bucket[b].pop()
                    break
                        
        # Count number of unique elements 
        ans = 0
        for b in range(len(bucket)):
            if bucket[b]:
                ans += len(bucket[b])
        
        return ans
                
        
        
        
        