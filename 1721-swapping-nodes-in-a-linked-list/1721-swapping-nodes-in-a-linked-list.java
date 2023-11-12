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
        ListNode slow = head;
        ListNode fast = head;
        ListNode first = head;
        ListNode second = head;

        // Get the first listnode, which is kth node from the beginning
        for (int i = 1; i < k; i++) {
            fast = fast.next;
        }
        first = fast;

        // Find the second listnode, which is the kth node from the end
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        second = slow;

        // Swap value
        int temp = first.val;
        first.val = second.val;
        second.val = temp;

        return head;
    }
}