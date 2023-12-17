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
import java.util.LinkedList;
import java.util.Stack;

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        if (root == null) {
            return res;
        }
        Stack<TreeNode> s = new Stack<>();
        s.push(root);
        
        while (!s.isEmpty()) {
            TreeNode tmp = s.pop();
            res.add(tmp.val);
            
            if (tmp.right != null) {
                s.push(tmp.right);
            }
            
            if (tmp.left != null) {
                s.push(tmp.left);
            }
        }
        
        return res;
    }
}