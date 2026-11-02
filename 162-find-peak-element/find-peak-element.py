class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 2

        while l <= r:
            mid = (l+r)//2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1

        return l