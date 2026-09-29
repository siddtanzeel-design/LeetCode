class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] != i:
                return i
        return n