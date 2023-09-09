from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = Counter(s)
        
        # Initialize a bucket
        bucket = [[] for i in range(len(s) + 1)]

        # Fill the bucket
        for c in char_counts:
            freq = char_counts[c]
            for i in range(freq):
                bucket[freq].append(c)

        new_string = ""
        for i in range(len(bucket) - 1, 0, -1):
            for y in bucket[i]:
                new_string += y

        return new_string