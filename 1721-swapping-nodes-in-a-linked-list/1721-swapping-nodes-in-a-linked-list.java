/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        List<ListNode> nodes = new ArrayList<>();
        
        ListNode tail = head;      
        while (tail != null) {
            nodes.add(tail);
            tail = tail.next;
        }
        
        ListNode left = nodes.get(k - 1);
        int temp = left.val;
        ListNode right = nodes.get(nodes.size() - k);
        left.val = right.val;
        right.val = temp;
        
        return head;
    }
}