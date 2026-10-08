class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        res = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[res-2]:
                nums[res] = nums[i]
                res += 1

        return res