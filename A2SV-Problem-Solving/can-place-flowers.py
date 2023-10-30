class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newbed = [0] + flowerbed + [0]
        N = len(newbed)
        
        for i in range(1, N-1):
            if newbed[i-1] == 0 and newbed[i] == 0 and newbed[i+1] == 0:
                newbed[i] = 1
                n -= 1
        return n <= 0