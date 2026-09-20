class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            var = nums[i]
            com = target - var

            if com in seen:
                return [seen[com], i]

            seen[var] = i