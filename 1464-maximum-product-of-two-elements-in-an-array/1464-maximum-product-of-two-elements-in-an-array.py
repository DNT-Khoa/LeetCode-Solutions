class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        max_val = 0
        
        for i in range(size):
            for j in range(i + 1, size):
                max_val = max(max_val, (nums[i] - 1) * (nums[j] - 1))
        
        return max_val