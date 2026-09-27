class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        element_count = Counter(nums)

        maj_element = []
        threshold = len(nums)//3

        for element, count in element_count.items():
            if count > threshold:
                maj_element.append(element)

        return maj_element