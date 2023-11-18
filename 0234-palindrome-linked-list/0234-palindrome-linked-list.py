# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle node
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        
        # Reverse the nodes starting from the middle node
        prev = None
        while mid:
            next = mid.next
            mid.next = prev
            prev = mid
            mid = next
        
        head2 = prev
        while head2:
            if head.val != head2.val:
                return False
            head2 = head2.next
            head = head.next
        
        return True