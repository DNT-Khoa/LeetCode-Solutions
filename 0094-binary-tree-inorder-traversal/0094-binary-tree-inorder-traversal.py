# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = deque()
        curr = root
        
        while curr or stack:
            # add all left nodes of curr to the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        
        return ans