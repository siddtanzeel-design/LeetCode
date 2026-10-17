class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digitSum(num):
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            return total

        def sortKey(num):
            return (digitSum(num), num)

        sorted_nums = sorted(nums, key=sortKey)

        n = len(nums)
        swaps = 0

        # Map each number to its target position
        position = {}

        for i in range(n):
            position[sorted_nums[i]] = i

        i = 0

        while i < n:
            while position[nums[i]] != i:
                target = position[nums[i]]

                nums[i], nums[target] = nums[target], nums[i]
                swaps += 1

            i += 1

        return swaps