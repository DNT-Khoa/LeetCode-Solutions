"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {None: None}
        
        # Create a new node for every original node and map them
        temp = head
        while temp:
            newNode = Node(temp.val)
            nodeMap[temp] = newNode
            temp = temp.next
        
        # Copy the connections between the original nodes to the copy nodes
        temp = head
        while temp:
            copiedNode = nodeMap[temp]
            copiedNode.next = nodeMap[temp.next]
            copiedNode.random = nodeMap[temp.random]
            temp = temp.next
        
        return nodeMap[head]