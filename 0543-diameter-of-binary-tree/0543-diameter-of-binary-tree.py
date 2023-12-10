# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDepth = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.maxDepth
    
    def depth(self, node):
        lDepth = self.depth(node.left) if node.left else 0
        rDepth = self.depth(node.right) if node.right else 0
        self.maxDepth = max(self.maxDepth, lDepth + rDepth)
        
        return 1 + (lDepth if lDepth > rDepth else rDepth)
        