class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeropos = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[zeropos] = nums[zeropos], nums[i]
                zeropos+=1