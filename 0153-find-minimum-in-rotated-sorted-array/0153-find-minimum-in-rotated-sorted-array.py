class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lastNum = nums[-1]
        l, r = 0, n-1 
        
        while l < r:
            m = l + (r - l) // 2
            
            if nums[m] > lastNum:
                l = m + 1
            else:
                r = m
        
        return nums[l]