# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque()
        queue.append(root)
        
        while queue:
            times = len(queue)
            xExists = yExists = False
            for _ in range(times):
                node = queue.popleft()
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False
                
                if node.val == x:
                    xExists = True
                if node.val == y:
                    yExists = True
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if xExists and yExists:
                return True
        
        return False
                