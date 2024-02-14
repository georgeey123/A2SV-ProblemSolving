class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        pivot = float("inf")
        index = 0
        next_largest, check = 0, 0
        for right in range(len(arr)-2, -1, -1):
            if arr[right] > arr[right+1]:
                next_largest = right
                break
        
        for index in range(next_largest+1, len(arr)):
            if 0 < arr[next_largest] - arr[index] < pivot:
                pivot = arr[next_largest] - arr[index]
                check = index

        
        arr[next_largest], arr[check] =  arr[check], arr[next_largest]
        return arr
            