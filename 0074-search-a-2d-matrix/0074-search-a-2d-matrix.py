class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def convertIndex(index):
            x = index % len(matrix[0])
            y = index // len(matrix[0])
            return matrix[y][x]
            
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            num = convertIndex(m)
            
            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                return True
                
        return False
                