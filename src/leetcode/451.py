from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)  # Step 1: Count frequency
        sorted_chars = sorted(freq.keys(), key=lambda x: -freq[x])  # Step 2: Sort
        return "".join(char * freq[char] for char in sorted_chars)  # Step 3: Build output

