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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        Stack<TreeNode> s = new Stack<>();
        TreeNode currNode = root;
        boolean done = false;
        
        while (!done) {
            if (currNode != null) {
                s.push(currNode);
                currNode = currNode.left;
            } else {
                if (s.isEmpty()) {
                    done = true;
                } else {
                    currNode = s.pop();
                    res.add(currNode.val);
                    currNode = currNode.right;
                }
            }
        }
        
        return res;
    }
}