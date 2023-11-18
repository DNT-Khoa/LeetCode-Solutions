# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get the pointer to the kth node from the beginning
        first = head
        for i in range(k-1):
            first = first.next
        
        # Get the pointer to the kth node from the end
        second = head
        fast = first
        
        while fast.next:
            second = second.next
            fast = fast.next
        
        # Swap the value of first and second node
        temp = first.val
        first.val = second.val
        second.val = temp
        
        return head