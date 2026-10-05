class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = heights.copy()
        expected.sort()

        c = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                c+=1

        return c