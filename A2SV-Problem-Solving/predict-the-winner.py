class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def score(left, right):

            if left > right:
                return 0

            state = (left, right)
            if state not in memo:
                player1_score = nums[left] - score(left + 1, right)
                player2_score = nums[right] - score(left, right - 1)
                memo[state] = max(player1_score, player2_score)

            return memo[state]

        return score(0, n-1) >= 0