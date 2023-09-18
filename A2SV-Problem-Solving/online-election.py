class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.candidates = []
        candidate = -1
        count = Counter()

        for idx, person in enumerate(persons):
            count[person] += 1
            if count[person] >= count[candidate]:
                candidate = person
            self.candidates.append(candidate)

    def q(self, t: int) -> int:
        res = bisect_right(self.times, t)
        return self.candidates[res - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)