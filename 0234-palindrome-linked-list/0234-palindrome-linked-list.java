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
    public boolean isPalindrome(ListNode head) {
        if (head == null) {
            return false;
        }
        
        // Find mid point
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode midPoint = slow;
        
        // Reverse the nodes starting from mid point
        ListNode prev = null;
        ListNode next = null;
        while (midPoint != null) {
            next = midPoint.next;
            midPoint.next = prev;
            prev = midPoint;
            midPoint = next;
        }
        
        // Check for palindrome
        ListNode left = head;
        ListNode right = prev;
        while (left != null && right != null) {
            if (left.val != right.val) {
                return false;
            }
            
            left = left.next;
            right = right.next;
        }
        
        return true;
    }
}