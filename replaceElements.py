class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_max = -1

        for i in range(len(arr) -1, -1, -1):
            new_max = max(last_max, arr[i])
            arr[i] = last_max
            last_max = new_max
        
        return arr
