class Solution:
    def findMedianSortedArrays(self, num1, num2):
        merged = num1 + num2

        merged.sort()

        n = len(merged)
        if n%2 == 0:
            median = (merged[n//2-1] + merged[n//2])/2
        else:
            median = merged[n//2]

        return median