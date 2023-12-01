class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set2 = set()
        ans = set()
        
        for num in nums2:
            set2.add(num)
            
        for num in nums1:
            if num in set2:
                ans.add(num)
        
        return list(ans)