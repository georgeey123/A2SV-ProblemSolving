class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj_elements = []
        list_size = len(nums)

        for i, j in Counter(nums).items():
            if j > list_size / 3:
                maj_elements.append(i)

        return maj_elements
