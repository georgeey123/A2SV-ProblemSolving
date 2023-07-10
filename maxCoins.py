class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum_ = 0
        pile_length = len(piles)
        for i in range(pile_length // 3):
            sum_ += piles[-2 - 2*i]
        return sum_



