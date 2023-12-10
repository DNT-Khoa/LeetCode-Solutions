/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        int heightLeft = root.left != null ? getHeight(root.left) + 1 : 0;
        int heightRight = root.right != null ? getHeight(root.right) + 1 : 0;
        int distance = Math.abs(heightLeft - heightRight);
        
        boolean leftBalanced = true;
        boolean rightBalanced = true;
        if (root.left != null) {
            leftBalanced = isBalanced(root.left);
        }
        if (root.right != null) {
            rightBalanced = isBalanced(root.right);
        }
        
        return distance <= 1 && leftBalanced && rightBalanced;
    }
    
    public static int getHeight(TreeNode node) {
        int leftHeight = node.left != null ? getHeight(node.left) + 1 : 0;
        int rightHeight = node.right != null ? getHeight(node.right) + 1 : 0;
        
        if (leftHeight > rightHeight) {
            return leftHeight;
        } else {
            return rightHeight;
        }
    }
}