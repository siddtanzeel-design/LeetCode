class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            x = (low + high) // 2
            y = (m + n + 1) // 2 - x

            l1 = float('-inf') if x == 0 else nums1[x - 1]
            r1 = float('inf') if x == m else nums1[x]

            l2 = float('-inf') if y == 0 else nums2[y - 1]
            r2 = float('inf') if y == n else nums2[y]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)

            elif l1 > r2:
                high = x - 1
            else:
                low = x + 1