class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c_list = []
        stack = []
        
        for c in s:
            if c == '(':
                if stack:
                    c_list.append(c)
                stack.append(c)
            elif c == ')':
                stack.pop()
                
                if stack:
                    c_list.append(c)
                    
        return "".join(c_list)
    
    
# Time complexity: O(n)