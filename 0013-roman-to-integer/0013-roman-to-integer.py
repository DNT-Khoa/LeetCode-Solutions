class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0;
        board = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        prev = 0
        
        for i in range(len(s)-1, -1, -1):
            curr_val = board[s[i]]
            if curr_val < prev:
                res -= curr_val
            else:
                res += curr_val
            prev = curr_val
        
        return res
            