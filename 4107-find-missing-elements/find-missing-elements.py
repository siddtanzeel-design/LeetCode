class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        num2 = []

        for i in range(len(nums) - 1):
            for j in range(nums[i] + 1, nums[i+1]):
                num2.append(j)

        return num2