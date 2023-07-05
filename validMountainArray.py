class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        pointer = 0

        while pointer < len(arr) - 1 and arr[pointer] < arr[pointer+1]:
            pointer += 1

        if pointer == 0 or pointer == len(arr) - 1:
            return False

        while pointer < len(arr) - 1 and arr[pointer] > arr[pointer+1]:
            pointer += 1

        return pointer == len(arr) - 1
