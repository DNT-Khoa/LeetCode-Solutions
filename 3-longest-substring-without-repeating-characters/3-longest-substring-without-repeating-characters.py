class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        ptr_1 = ptr_2 = max_length = 0
        
        while ptr_2 < len(s):
            if not s[ptr_2] in my_set:
                my_set.add(s[ptr_2])
                max_length = max(max_length, len(my_set))
                ptr_2 += 1
            else:
                my_set.remove(s[ptr_1])
                ptr_1 += 1
                
        return max_length
    
    
# Time complexity: O(n)