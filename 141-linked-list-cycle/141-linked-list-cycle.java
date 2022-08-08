/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // Floyd cycle dectection
        ListNode slowP = head, fastP = head;
        
        while (slowP != null && fastP != null && fastP.next != null) {
            slowP = slowP.next;
            fastP = fastP.next.next;
            
            if (slowP == fastP) {
                return true;
            }
        }
        
        return false;
    }
}

// Time complexity: O(n)
// Space complexity: O(1)