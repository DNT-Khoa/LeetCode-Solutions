class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x > 0 and x % 10 == 0):
            return False
        
        oldX = x
        newX = 0
        
        while x > 0:
            newX = newX * 10 + x % 10
            x = x // 10
        
        return oldX == newX