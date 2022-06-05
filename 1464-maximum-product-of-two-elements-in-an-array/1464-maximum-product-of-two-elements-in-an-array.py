class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Find the largest and second largest number then multiply them
        a = b = 0 
        
        for num in nums:
            if num > b: 
                a, b = b, num
            elif num > a:
                a = num
                
        return (a - 1) * (b - 1)
        