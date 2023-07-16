class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            remaining_weight = limit - people[r]
            r -= 1
            boats += 1

            if l<=r and remaining_weight >=  people[l]:
                l += 1
        return boats
