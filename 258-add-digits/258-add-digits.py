class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num:
                total += num % 10
                num //= 10
            num = total 
        
        return num
    
    
"""
Another creative solution:
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            return 9 if num % 9 == 0 else num % 9
"""
                
            
            
        
        
   
        
            
