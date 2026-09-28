class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]*n

        product = 1
        for i in range(n):
            result[i] = product
            product *= nums[i]

            #[1,1,2,6]
        
        product = 1
        for i in range(n-1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result
