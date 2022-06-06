class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        size = len(nums)
        target = []
        
        for i in range(size):
            target.insert(index[i], nums[i])
            
        return target