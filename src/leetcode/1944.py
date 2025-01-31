class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []

        for i in range(len(heights) - 1, -1, -1):

            c = 0
            h = heights[i]
            while stack and stack[-1] < h:
                c += 1
                stack.pop()

            heights[i] = c + (1 if len(stack) != 0 else 0)
            stack.append(h)

        return heights

