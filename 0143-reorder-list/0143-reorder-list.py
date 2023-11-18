# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next        
        # Revert the nodes starting from middle node
        prev = None
        while middle:
            next = middle.next
            middle.next = prev
            prev = middle
            middle = next
        slow.next = None
        
        # Reorder list
        l1 = head
        l2 = prev
        
        while l2:
            next1 = l1.next
            next2 = l2.next
            
            l1.next = l2
            l2.next = next1
            
            l1 = next1
            l2 = next2
    