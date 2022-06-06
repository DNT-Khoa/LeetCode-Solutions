class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # Reverse of XOR is also XOR
        arr = [first]
        
        for i in encoded:
            arr.append(i ^ arr[-1])
            
        return arr