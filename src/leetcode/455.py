class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort children's greed factors
        s.sort()  # Sort cookie sizes

        i, j = 0, 0  # Child and cookie pointers

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # If the cookie can satisfy the child
                i += 1  # Move to next child
            j += 1  # Move to next cookie

        return i  # The number of content children

# solution 2
from bisect import bisect_left

class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        index = 0  # Pointer for cookies
        count = 0  # Number of satisfied children

        for greed in g:
            index = bisect_left(s, greed, index)  # Find smallest valid cookie
            if index < len(s):  # If a cookie is found
                count += 1
                index += 1  # Move to next cookie

        return count
