# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = deque()
        stack = deque()
        node = root
        
        while node or stack:
            if node:
                stack.append(node)
                ans.appendleft(node.val)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        
        return list(ans)