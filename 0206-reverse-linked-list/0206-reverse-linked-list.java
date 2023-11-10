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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode tail = head;
        
        while (tail != null) {
            ListNode next = tail.next;
            tail.next = prev;
            prev = tail;
            tail = next;
        }
        
        return prev;
    }
    
    // Time complexity: O(n)
    // Space complexity: O(1)
}