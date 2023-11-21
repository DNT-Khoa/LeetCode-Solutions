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
        nodeMap = {}
        
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
            copiedNode.next = nodeMap[temp.next] if temp.next else None
            copiedNode.random = nodeMap[temp.random] if temp.random else None
            temp = temp.next
        
        return nodeMap[head] if head else None