class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i