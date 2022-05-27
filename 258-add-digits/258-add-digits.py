class Solution:
    def sub_add_digits(self, n):
        quotient = n // 10
        
        if quotient == 0:
            return n
        remainder = n % 10
        
        return remainder + self.sub_add_digits(quotient)
    
    def addDigits(self, num: int) -> int:
        """
            38 // 10 => q = 3, r = 8
            keep dividing the number by 10 until q = 0
        """
        sub_sum = self.sub_add_digits(num)
        
        if sub_sum // 10 == 0:
            return sub_sum
        
        return self.addDigits(sub_sum)
        
        
   
        
            
