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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode start = dummy;
        int carrier = 0;
        
        while (l1 != null && l2 != null) {
            int number = l1.val + l2.val + carrier;
            int lastDigit = number % 10;
            carrier = number >= 10 ? 1 : 0;
            
            dummy.next = new ListNode(lastDigit);
            dummy = dummy.next;
            
            l1 = l1.next;
            l2 = l2.next;
        }
        
        while (l1 != null || l2 != null) {
            int number = l1 == null ? l2.val + carrier : l1.val + carrier;
            int lastDigit = number % 10;
            carrier = number >= 10 ? 1 : 0;
            
            dummy.next = new ListNode(lastDigit);
            dummy = dummy.next;
            
            if (l1 != null) {
                l1 = l1.next;
            } else {
                l2 = l2.next;
            }
        }
        
        if (carrier == 1) {
            dummy.next = new ListNode(1);
        }
        
        return start.next;
    }
}