class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        results = []

        for s in strs:
            sorted_s = sorted(s)
            sorted_s = ''.join(sorted_s)

            if sorted_s in dictionary:
                dictionary[sorted_s].append(s)
            else:
                dictionary[sorted_s] = [s]

        for k in dictionary:
            results.append(dictionary[k])

        return results