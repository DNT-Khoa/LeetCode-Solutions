class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        comparator = strs[0]

        for i in range(len(comparator)):
            for str in strs[1:]:
                if i == len(str) or comparator[i] != str[i]:
                    return ans
            ans += comparator[i]
        
        return ans