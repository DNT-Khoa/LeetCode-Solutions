# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Use DFS to traverse the tree
        stack = deque()
        stack.append(cloned)
        
        while len(stack) > 0:
            current = stack.pop()
            if current.val == target.val:
                return current
            
            right, left = current.right, current.left
            if right:
                stack.append(right)
            if left:
                stack.append(left)
        
        return None