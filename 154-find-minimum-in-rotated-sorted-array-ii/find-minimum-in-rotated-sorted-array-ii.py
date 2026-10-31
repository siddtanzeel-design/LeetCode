class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l + r)//2

            if nums[mid] < nums[r]:
                r = mid

            elif nums[mid] == nums[r]:
                r -= 1
            
            else:
                l = mid + 1

        return nums[r]