from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right = [1] * N, [1] * N
        
        # Fill left array
        for i in range(1, N):
            left[i] = left[i - 1] * nums[i - 1]
        
        # Fill right array
        for i in range(N - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # Another loop
        for i in range(N):
            nums[i] = left[i] * right[i]
            
        return nums