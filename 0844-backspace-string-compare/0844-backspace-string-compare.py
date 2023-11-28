from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = deque()
        
        for c in s:
            if c != "#":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        s = "".join(stack)
        
        stack.clear()
        
        for c in t:
            if c != "#":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        t = "".join(stack)
        
        return s == t