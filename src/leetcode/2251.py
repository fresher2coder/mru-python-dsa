class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        bloom = sorted(start for start, _ in flowers)  # Sort bloom days
        wither = sorted(end + 1 for _, end in flowers)  # Sort wither days

        result = []
        for person in people:
            blooming = bisect_right(bloom, person)  # Flowers that started blooming
            wilted = bisect_right(wither, person)  # Flowers that have withered
            result.append(blooming - wilted)  # Active flowers = blooming - wilted

        return result