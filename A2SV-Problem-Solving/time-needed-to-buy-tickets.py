class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque([i,v] for i,v in enumerate(tickets))
        total = 0

        while True:
            i, v = tickets.popleft()
            total += 1

            if i == k and v - 1 == 0:
                return total

            if v > 1:
                tickets.append([i, v- 1])