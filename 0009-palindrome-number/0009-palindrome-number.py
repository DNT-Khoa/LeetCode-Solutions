class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        store = []
        
        while x != 0:
            store.append(x % 10)
            x = x // 10
        
        for i in range(len(store)):
            if store[i] != store[len(store) - i - 1]:
                return False
            
        return True