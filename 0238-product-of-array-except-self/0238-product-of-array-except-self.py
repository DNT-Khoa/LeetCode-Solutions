from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr, suffix_arr = [], []
        
        # Fill prefix array
        prod = 1
        for i, n in enumerate(nums):
            if i == 0:
                pass
            else:
                prod *= nums[i - 1]
            prefix_arr.append(prod)
            
        # Fill suffix array
        prod = 1
        for i, n in reversed(list(enumerate(nums))):
            if i == len(nums) - 1:
                pass
            else:
                prod *= nums[i + 1]
            suffix_arr = [prod] + suffix_arr
            
        for i in range(len(nums)):
            nums[i] = prefix_arr[i] * suffix_arr[i]
        
        return nums