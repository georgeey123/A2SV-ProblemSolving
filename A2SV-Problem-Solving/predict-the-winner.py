class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        def score(left, right):

            if left > right:
                return 0

            player1_score = nums[left] - score(left + 1, right)
            player2_score = nums[right] - score(left, right - 1)


            return max(player1_score, player2_score)

        return score(0, n-1) >= 0