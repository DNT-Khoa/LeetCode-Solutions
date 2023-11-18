# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        # Find nth node from the start
        p1 = p2 = head
        for _ in range(n - 1):
            p2 = p2.next
        
        # Find the nth node from the end
        while p2.next:
            prev = p1
            p1 = p1.next
            p2 = p2.next
        
        prev.next = prev.next.next # remove the nth node from the end
        return dummy.next