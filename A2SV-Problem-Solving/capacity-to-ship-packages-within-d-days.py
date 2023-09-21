class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = right

        def canShip(mid):
            ships, cur_weight = 1, mid

            for weight in weights:
                if cur_weight - weight < 0:
                    ships += 1
                    cur_weight = mid
                cur_weight -= weight
            return ships <= days

        while left <= right:
            mid = left + (right - left) // 2

            if canShip(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result