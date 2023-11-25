class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

'''
Using dummy nodes as left and right nodes is very useful
for this question because it can help you avoid checking
if node is tail or head 
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        # Remove node from LL
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        # Remove the node from map
        del self.map[node.key]
    
    def append(self, node):
        # Append node to end of LL
        prev = self.right.prev
        node.next = self.right
        node.prev = prev
        prev.next = node
        self.right.prev = node
        
        # Append node to map
        self.map[node.key] = node
        
    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node) 
            self.append(node)
            
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
        self.append(Node(key, value))
        
        if len(self.map) > self.capacity:
            self.remove(self.left.next)
        
        
        
        