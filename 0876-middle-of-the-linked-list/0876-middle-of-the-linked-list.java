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
    public ListNode middleNode(ListNode head) {
        List<ListNode> store = new ArrayList<>();
        
        ListNode temp = head;
        
        while (temp != null) {
            store.add(temp);
            temp = temp.next;
        }
        
        return store.get(store.size() / 2);
    }
}