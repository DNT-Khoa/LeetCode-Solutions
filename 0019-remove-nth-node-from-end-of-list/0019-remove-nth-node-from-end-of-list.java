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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = null;
        
        // Move the next node nth nodes from the beginning
        for (int i = 1; i < n; i++) {
            fast = fast.next;
        }
        
        // Move the fast to the end of the link
        while (fast.next != null) {
            prev = slow;
            fast = fast.next;
            slow = slow.next;
        }
        
        if (prev == null) {
            head = slow.next;
        } else {
            prev.next = prev.next.next;
            return head;
        }

        return head;
    }
}