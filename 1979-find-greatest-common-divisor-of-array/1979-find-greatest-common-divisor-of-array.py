class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        
        return gcd(b, a % b)
        
        
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))
    