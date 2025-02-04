import heapq
from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Count the frequency of each barcode
        barcode_counts = Counter(barcodes)

        # Build a max-heap based on the negative counts
        max_heap = [(-count, barcode) for barcode, count in barcode_counts.items()]
        heapq.heapify(max_heap)

        n = len(barcodes)
        result = [0] * n
        index = 0

        # Place barcodes based on frequency
        while max_heap:
            count, barcode = heapq.heappop(max_heap)
            for _ in range(-count):
                result[index] = barcode
                index += 2
                if index >= n:
                    index = 1

        return result