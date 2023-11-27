class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find index of smallest num in the list
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            
            if nums[m] <= nums[-1]:
                r = m
            else:
                l = m + 1
        
        if target == nums[l]:
            return l
        # Target search range where target exists
        pivotIdx = l
        l, r = 0, len(nums) - 1
        if nums[-1] == nums[pivotIdx]:
            r -= 1
        else:
            if target <= nums[-1]:
                l = pivotIdx
            else:
                r = pivotIdx
        
        # Now find target in new range
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
            
            
            