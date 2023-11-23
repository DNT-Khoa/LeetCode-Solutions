class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Imagine nums is a linked list
        # val of node = index of list item
        # next of node = val of list item
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
        