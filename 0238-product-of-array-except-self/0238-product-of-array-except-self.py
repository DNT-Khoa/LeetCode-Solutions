from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = reduce(lambda a, b: a * (b if b else 1), nums, 1), nums.count(0)
        
        if zero_count > 1:
            return [0] * len(nums)
        else:
            for idx, num in enumerate(nums):
                if zero_count == 1:
                    if num == 0:
                        nums[idx] = prod
                    else:
                        nums[idx] = 0
                else:
                    nums[idx] = prod // num
        return nums