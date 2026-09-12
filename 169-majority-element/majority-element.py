class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        majorEle = nums[0]
        maxCount = 1
        count = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                count += 1
            else:
                if count > maxCount:
                    maxCount = count
                    majorEle = nums[i]
                count = 1

        if count > maxCount:
            majorEle = nums[-1]

        return majorEle