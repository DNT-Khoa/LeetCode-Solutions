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
import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<List<Integer>> ans = new ArrayList<>();
        Queue<TreeNode> mq = new LinkedList<>();
        mq.add(root);
        
        while (!mq.isEmpty()) {
            List<Integer> currLevel = new ArrayList<>();
            int times = mq.size();
            
            for (int i = 0; i < times; i++) {
                TreeNode node = mq.remove();
                currLevel.add(node.val);
                if (node.left != null) {
                    mq.add(node.left);
                }
                if (node.right != null) {
                    mq.add(node.right);
                }
            }
            ans.add(currLevel);
        }
        
        return ans;
    }
}