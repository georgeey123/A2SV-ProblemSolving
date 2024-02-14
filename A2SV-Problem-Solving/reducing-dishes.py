class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        res, cur_sum = 0, 0

        for i in range(len(satisfaction)):
            cur_sum += satisfaction[i]
            if cur_sum < 0:
                break
            
            res += cur_sum

        return res