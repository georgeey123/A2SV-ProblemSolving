class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        checked = set()
        for i in arr:
            if i/2 in checked or i * 2 in checked:
                return True
            checked.add(i)
        return False
            
