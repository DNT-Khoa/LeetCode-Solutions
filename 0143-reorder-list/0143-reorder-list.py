# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        
        # Revert the nodes starting from middle node
        prev = None
        while middle:
            next = middle.next
            middle.next = prev
            prev = middle
            middle = next
        
        # Reorder list
        l1 = head
        l2 = prev
        
        while l1 and l2 and l1 is not l2:
            next = l1.next
            l1.next = l2
            l1 = l2
            l2 = next
            
            if l1 is l2:
                l1.next = None
    